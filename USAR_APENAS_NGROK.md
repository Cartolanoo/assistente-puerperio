# 🚇 Como Usar Apenas o NGROK

Este guia mostra como rodar o projeto **apenas localmente com NGROK**, sem precisar de Railway ou Render.

## 📋 Pré-requisitos

1. **Python 3.8+** instalado
2. **NGROK** instalado (veja abaixo)
3. **Chave do Gemini** (obrigatória)

## 🚀 Passo a Passo Rápido

### 1. Instalar NGROK

#### Opção A: Baixar e Colocar na Pasta do Projeto (Mais Simples)

1. Baixe: https://ngrok.com/download
2. Extraia o `ngrok.exe`
3. Coloque na pasta do projeto: `C:\Users\Cartolano\Documents\chatbot-puerperio\ngrok.exe`

#### Opção B: Instalar Globalmente

1. Baixe o ngrok
2. Extraia para `C:\ngrok\`
3. Adicione `C:\ngrok\` ao PATH do Windows

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_gemini_aqui
SECRET_KEY=sua-chave-secreta-aqui
FLASK_ENV=development
PORT=5000
```

### 3. Instalar Dependências

```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 4. Iniciar o Servidor

#### Opção A: Usar o Script Automático (Recomendado)

```bash
.\iniciar-com-ngrok.bat
```

Este script vai:
- ✅ Verificar se o Python está instalado
- ✅ Iniciar o servidor Flask na porta 5000
- ✅ Iniciar o NGROK automaticamente
- ✅ Mostrar o link público

#### Opção B: Manual (2 Terminais)

**Terminal 1 - Iniciar Flask:**
```bash
cd backend
python app.py
```

**Terminal 2 - Iniciar NGROK:**
```bash
ngrok http 5000
```

### 5. Acessar

Após iniciar, você verá algo como:

```
Forwarding  https://abc123.ngrok-free.app -> http://localhost:5000
```

Use esse link para acessar de qualquer lugar!

---

## 🎯 Quando Usar Apenas NGROK

### ✅ Perfeito Para:
- **Desenvolvimento local**
- **Testes rápidos**
- **Demonstrações temporárias**
- **Testar em dispositivos móveis**
- **Quando não precisa de URL permanente**

### ❌ Não Use Para:
- **Produção** (link expira)
- **Aplicação permanente** (link muda)
- **Quando precisa de URL fixa**

---

## 📱 Acessar do Celular

1. Certifique-se de que o celular está na **mesma rede WiFi** do computador
2. OU use o link do NGROK (funciona de qualquer lugar)
3. Acesse o link mostrado no terminal do NGROK

---

## ⚙️ Configurações Avançadas

### NGROK com Autenticação (Opcional)

Para ter links mais estáveis:

1. Crie conta gratuita: https://dashboard.ngrok.com/signup
2. Pegue seu authtoken no dashboard
3. Configure:
   ```bash
   ngrok config add-authtoken SEU_TOKEN_AQUI
   ```

### Mudar Porta

Se quiser usar outra porta (ex: 8080):

1. Edite `backend/app.py` linha 2409:
   ```python
   port = int(os.environ.get("PORT", 8080))
   ```

2. Inicie o NGROK na nova porta:
   ```bash
   ngrok http 8080
   ```

---

## 🔧 Troubleshooting

### "ngrok não encontrado"
- Verifique se `ngrok.exe` está na pasta do projeto
- OU adicione o ngrok ao PATH do Windows

### "Porta 5000 já em uso"
- Feche outros programas usando a porta 5000
- OU mude a porta (veja "Configurações Avançadas")

### Link do NGROK não funciona
- Verifique se o Flask está rodando
- Verifique se o NGROK está conectado
- Veja os logs no terminal

### Emails não funcionam via NGROK
- ⚠️ Links do NGROK podem cair no spam
- Configure email separadamente (veja `CONFIGURAR_EMAIL.md`)

---

## 📊 Resumo

| Item | Status |
|------|--------|
| **Instalação** | ⚠️ Requer baixar ngrok.exe |
| **Configuração** | ✅ Simples (só .env) |
| **Uso** | ✅ Script automático ou manual |
| **URL** | ⚠️ Temporária (expira) |
| **Custo** | ✅ Gratuito |
| **Ideal Para** | Desenvolvimento e testes |

---

## ✅ Checklist Rápido

- [ ] NGROK baixado (`ngrok.exe` na pasta)
- [ ] Arquivo `.env` criado com `GEMINI_API_KEY`
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Script `iniciar-com-ngrok.bat` funciona
- [ ] Servidor Flask inicia sem erros
- [ ] NGROK mostra link público
- [ ] Consegue acessar pelo link

---

## 🎉 Pronto!

Agora você pode usar apenas o NGROK para desenvolvimento local. 

**Não precisa de Railway ou Render** se quiser apenas testar localmente! 🚀
