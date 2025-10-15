import os
import json
import random
import difflib
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa o Flask
app = Flask(__name__)

# Configurações
BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "dados")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializa cliente OpenAI se a chave estiver disponível
client = None
if OPENAI_API_KEY:
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception as e:
        print(f"AVISO: Erro ao inicializar cliente OpenAI: {e}")
        client = None

# Carrega os arquivos JSON
def carregar_dados():
    try:
        with open(os.path.join(BASE_PATH, "base_conhecimento.json"), "r", encoding="utf-8") as f:
            base = json.load(f)
        
        with open(os.path.join(BASE_PATH, "mensagens_apoio.json"), "r", encoding="utf-8") as f:
            apoio = json.load(f)
        
        with open(os.path.join(BASE_PATH, "alertas.json"), "r", encoding="utf-8") as f:
            alertas = json.load(f)
        
        return base, apoio, alertas
    except FileNotFoundError as e:
        print(f"Erro ao carregar arquivos: {e}")
        return {}, {}, {}

# Carrega os dados
base_conhecimento, mensagens_apoio, alertas = carregar_dados()

# Histórico de conversas (em produção, usar banco de dados)
conversas = {}

# Palavras-chave para alertas
palavras_alerta = ["sangramento", "febre", "dor", "inchaço", "tristeza", "depressão", "emergência"]

class ChatbotPuerperio:
    def __init__(self):
        self.base = base_conhecimento
        self.apoio = mensagens_apoio
        self.alertas = alertas
        self.client = client
    
    def verificar_alertas(self, pergunta):
        """Verifica se a pergunta contém palavras que indicam necessidade de atenção médica"""
        pergunta_lower = pergunta.lower()
        alertas_encontrados = []
        
        for palavra in palavras_alerta:
            if palavra in pergunta_lower:
                alertas_encontrados.append(palavra)
        
        return alertas_encontrados
    
    def buscar_resposta_local(self, pergunta):
        """Busca resposta na base de conhecimento local"""
        pergunta_lower = pergunta.lower()
        melhor_match = None
        maior_similaridade = 0
        categoria = None
        
        for tema, conteudo in self.base.items():
            pergunta_base = conteudo["pergunta"].lower()
            similaridade = difflib.SequenceMatcher(None, pergunta_lower, pergunta_base).ratio()
            
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                melhor_match = conteudo["resposta"]
                categoria = tema
        
        if maior_similaridade > 0.5:
            return melhor_match, categoria, maior_similaridade
        
        return None, None, 0
    
    def gerar_resposta_openai(self, pergunta, contexto=""):
        """Gera resposta usando OpenAI se disponível"""
        if not self.client:
            return None
        
        try:
            system_message = """Você é um assistente especializado em saúde materna e puerpério. 
            Forneça informações empáticas, acolhedoras e baseadas em evidências científicas.
            Sempre encoraje a busca por atendimento médico quando necessário.
            Use linguagem simples e acolhedora."""
            
            if contexto:
                system_message += f"\n\nContexto adicional: {contexto}"
            
            resposta = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": pergunta}
                ],
                max_tokens=500,
                temperature=0.7
            )
            return resposta.choices[0].message.content
        except Exception as e:
            print(f"Erro ao chamar OpenAI: {e}")
            return None
    
    def chat(self, pergunta, user_id="default"):
        """Função principal do chatbot"""
        # Verifica alertas
        alertas_encontrados = self.verificar_alertas(pergunta)
        
        # Busca resposta local primeiro
        resposta_local, categoria, similaridade = self.buscar_resposta_local(pergunta)
        
        # Se encontrou resposta local com boa similaridade, usa ela
        if resposta_local and similaridade > 0.7:
            resposta_final = resposta_local
            fonte = "base_conhecimento"
        else:
            # Tenta OpenAI se disponível
            resposta_openai = self.gerar_resposta_openai(pergunta)
            if resposta_openai:
                resposta_final = resposta_openai
                fonte = "openai"
            elif resposta_local:
                resposta_final = resposta_local
                fonte = "base_conhecimento"
            else:
                resposta_final = random.choice(list(self.apoio.values()))
                fonte = "mensagem_apoio"
        
        # Adiciona alertas se necessário
        if alertas_encontrados:
            alertas_texto = []
            for alerta_key, alerta_texto in self.alertas.items():
                alertas_texto.append(alerta_texto)
            
            resposta_final += "\n\n**ALERTA IMPORTANTE:**\n" + "\n".join(alertas_texto)
        
        # Salva na conversa
        timestamp = datetime.now().isoformat()
        if user_id not in conversas:
            conversas[user_id] = []
        
        conversas[user_id].append({
            "timestamp": timestamp,
            "pergunta": pergunta,
            "resposta": resposta_final,
            "categoria": categoria,
            "fonte": fonte,
            "alertas": alertas_encontrados
        })
        
        return {
            "resposta": resposta_final,
            "categoria": categoria,
            "fonte": fonte,
            "alertas": alertas_encontrados,
            "timestamp": timestamp
        }

# Inicializa o chatbot
chatbot = ChatbotPuerperio()

# Rotas da API
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json()
    pergunta = data.get('pergunta', '')
    user_id = data.get('user_id', 'default')
    
    if not pergunta.strip():
        return jsonify({"erro": "Pergunta não pode estar vazia"}), 400
    
    resposta = chatbot.chat(pergunta, user_id)
    return jsonify(resposta)

@app.route('/api/historico/<user_id>')
def api_historico(user_id):
    return jsonify(conversas.get(user_id, []))

@app.route('/api/categorias')
def api_categorias():
    categorias = list(base_conhecimento.keys())
    return jsonify(categorias)

@app.route('/api/alertas')
def api_alertas():
    return jsonify(alertas)

# Rota para teste
@app.route('/teste')
def teste():
    return jsonify({
        "status": "funcionando",
        "base_conhecimento": len(base_conhecimento),
        "mensagens_apoio": len(mensagens_apoio),
        "openai_disponivel": client is not None
    })

if __name__ == "__main__":
    print("Chatbot do Puerperio iniciado!")
    print("Base de conhecimento carregada:", len(base_conhecimento), "itens")
    print("Mensagens de apoio carregadas:", len(mensagens_apoio), "itens")
    print("OpenAI disponivel:", "Sim" if client else "Nao")
    print("Acesse: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

