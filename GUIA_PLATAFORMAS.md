# 🌐 Guia de Plataformas - Quando Usar Cada Uma

Este projeto está configurado para funcionar em **3 ambientes diferentes**. Escolha o melhor para cada situação:

## 🚂 Railway (Produção Principal) ⭐ RECOMENDADO

### ✅ Quando Usar:
- **Produção** - Aplicação em uso real
- **Deploy permanente** - URL fixa e estável
- **Alta disponibilidade** - Sempre online

### 📋 Configuração:
- ✅ Já configurado com `railway.json` e `Dockerfile`
- ✅ Variáveis de ambiente configuráveis no dashboard
- ✅ Deploy automático via GitHub

### 🔗 Links:
- Dashboard: https://railway.app
- Sua URL: Será gerada automaticamente (ex: `seu-projeto.up.railway.app`)

### 📝 Variáveis Necessárias:
```
SECRET_KEY=sua-chave-secreta
GEMINI_API_KEY=sua-chave-gemini
FLASK_ENV=production
```

---

## 🌐 Render (Backup/Alternativa)

### ✅ Quando Usar:
- **Backup** - Se o Railway tiver problemas
- **Testes** - Ambiente de teste separado
- **Comparação** - Testar diferentes configurações

### 📋 Configuração:
- ✅ Já configurado com `render.yaml`
- ✅ Deploy automático via GitHub
- ⚠️ App "dorme" após inatividade (plano gratuito)

### 🔗 Links:
- Dashboard: https://dashboard.render.com
- Sua URL: `assistente-puerperio.onrender.com`

### 📝 Variáveis Necessárias:
```
SECRET_KEY=sua-chave-secreta
GEMINI_API_KEY=sua-chave-gemini
FLASK_ENV=production
```

---

## 🚇 NGROK (Desenvolvimento Local)

### ✅ Quando Usar:
- **Desenvolvimento** - Testar localmente
- **Testes em mobile** - Acessar do celular na mesma rede
- **Demonstrações rápidas** - Compartilhar link temporário

### 📋 Configuração:
- ✅ Script `iniciar-com-ngrok.bat` já criado
- ⚠️ Requer instalação do ngrok.exe
- ⚠️ Link temporário (expira em algumas horas)

### 🔗 Como Usar:
1. **Instalar NGROK:**
   - Baixe: https://ngrok.com/download
   - Extraia `ngrok.exe` na pasta do projeto
   
2. **Iniciar:**
   ```bash
   # Windows
   .\iniciar-com-ngrok.bat
   
   # OU manualmente:
   python backend/app.py  # Terminal 1
   ngrok http 5000        # Terminal 2
   ```

3. **Acessar:**
   - Link será mostrado no terminal (ex: `https://abc123.ngrok.io`)

### ⚠️ Limitações:
- Link expira após algumas horas
- Pode cair no spam (emails)
- Não recomendado para produção

---

## 📊 Comparação Rápida

| Recurso | Railway | Render | NGROK |
|---------|---------|--------|-------|
| **Uso** | Produção | Backup/Teste | Desenvolvimento |
| **Custo** | Gratuito (limitado) | Gratuito (limitado) | Gratuito |
| **URL Fixa** | ✅ Sim | ✅ Sim | ❌ Não (temporária) |
| **Sempre Online** | ✅ Sim | ⚠️ "Dorme" (free) | ❌ Não (local) |
| **Deploy Auto** | ✅ Sim | ✅ Sim | ❌ Não |
| **Configuração** | ✅ Já configurado | ✅ Já configurado | ⚠️ Requer instalação |
| **Recomendado Para** | Produção | Backup | Desenvolvimento |

---

## 🎯 Recomendação Final

### Para Produção:
**Railway** → Principal
**Render** → Backup (opcional)

### Para Desenvolvimento:
**NGROK** → Testes locais rápidos
**Localhost** → Desenvolvimento normal

---

## 📚 Documentação Adicional

- **Railway**: Veja `DEPLOY_RAILWAY.md`
- **Render**: Veja `GUIA_DEPLOY_RAPIDO.md`
- **NGROK**: Veja `COMO_INSTALAR_NGROK.md` e `INICIAR_SERVIDORES.md`

---

## ✅ Status Atual

- ✅ Railway configurado e funcionando
- ✅ Render configurado (render.yaml pronto)
- ✅ NGROK configurado (scripts prontos)
- ✅ Todas as plataformas mantidas no projeto
