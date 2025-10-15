# 🤱 Assistente Puerpério

Um chatbot especializado em oferecer apoio e informações sobre o período pós-parto (puerpério), desenvolvido com foco na saúde materna e bem-estar das mães.

## ✨ Funcionalidades

- **💬 Chat Inteligente**: Sistema de respostas baseado em IA com fallback para base de conhecimento local
- **🚨 Sistema de Alertas**: Detecta automaticamente palavras-chave que indicam necessidade de atenção médica
- **📚 Base de Conhecimento**: Conteúdo especializado em puerpério, alimentação, baby blues e mais
- **📱 Interface Responsiva**: Design moderno e intuitivo, funcionando em desktop e mobile
- **📊 Categorização**: Organização por temas (identidade, alimentação, baby blues, etc.)
- **📝 Histórico de Conversas**: Mantém o histórico das conversas por usuário
- **🎯 Perguntas Rápidas**: Botões com perguntas frequentes para facilitar o uso

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **IA**: OpenAI GPT-4o-mini (opcional)
- **Estilização**: CSS customizado com gradientes e animações
- **Ícones**: Font Awesome

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd chatbot-puerperio
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   ```bash
   # Copie o arquivo de template
   copy .env.template .env
   
   # Edite o arquivo .env e adicione sua chave da OpenAI (opcional)
   OPENAI_API_KEY=sua_chave_aqui
   ```

5. **Execute o aplicativo**:
   ```bash
   cd backend
   python app.py
   ```

6. **Acesse no navegador**:
   ```
   http://localhost:5000
   ```

## 📁 Estrutura do Projeto

```
chatbot-puerperio/
├── backend/
│   ├── app.py                 # Aplicação Flask principal
│   ├── templates/
│   │   └── index.html         # Interface web
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Estilos da interface
│   │   └── js/
│   │       └── chat.js        # Lógica do frontend
│   └── dados/                 # Arquivos JSON com conhecimento
├── dados/                     # Base de conhecimento
│   ├── base_conhecimento.json
│   ├── mensagens_apoio.json
│   └── alertas.json
├── requirements.txt           # Dependências Python
├── .env.template             # Template de configuração
└── README.md                 # Este arquivo
```

## 🔧 Configuração da API OpenAI (Opcional)

O chatbot funciona perfeitamente sem a API da OpenAI, usando apenas a base de conhecimento local. Para habilitar respostas mais avançadas:

1. Crie uma conta na [OpenAI](https://openai.com)
2. Gere uma chave de API
3. Adicione no arquivo `.env`:
   ```
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

## 📊 Base de Conhecimento

O sistema inclui informações sobre:

- **Identidade**: Mudanças emocionais no puerpério
- **Alimentação**: Nutrição adequada pós-parto
- **Baby Blues**: Depressão pós-parto leve
- **Puerpério**: Conceitos gerais sobre o período

### Adicionando Conteúdo

Para expandir a base de conhecimento, edite o arquivo `dados/base_conhecimento.json`:

```json
{
  "nova_categoria": {
    "pergunta": "Sua pergunta aqui?",
    "resposta": "Resposta detalhada aqui."
  }
}
```

## 🚨 Sistema de Alertas

O sistema detecta automaticamente palavras que indicam necessidade de atenção médica:

- Sangramento
- Febre
- Dor
- Inchaço
- Tristeza
- Depressão
- Emergência

Quando detectadas, o sistema exibe alertas e oferece opções para contato médico.

## 🎨 Personalização

### Cores e Tema

Edite o arquivo `backend/static/css/style.css` para personalizar:

- Cores principais
- Gradientes
- Tipografia
- Animações

### Mensagens de Apoio

Modifique `dados/mensagens_apoio.json` para adicionar novas mensagens empáticas.

## 🔒 Segurança

- Chaves de API são carregadas de variáveis de ambiente
- Validação de entrada no backend
- Sanitização de mensagens
- Histórico local (não persistente)

## 🚀 Deploy

### Heroku

1. Crie um arquivo `Procfile`:
   ```
   web: python backend/app.py
   ```

2. Configure as variáveis de ambiente no Heroku

3. Faça o deploy:
   ```bash
   git push heroku main
   ```

### Docker

1. Crie um `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "backend/app.py"]
   ```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Para dúvidas ou problemas:

1. Verifique a documentação
2. Consulte as issues existentes
3. Crie uma nova issue com detalhes do problema

## 🙏 Agradecimentos

- Comunidade Python/Flask
- OpenAI pela API GPT
- Font Awesome pelos ícones
- Todas as mães que contribuíram com feedback

---

**⚠️ Aviso Importante**: Este chatbot é uma ferramenta de apoio e não substitui o acompanhamento médico profissional. Sempre consulte profissionais de saúde para questões médicas específicas.

