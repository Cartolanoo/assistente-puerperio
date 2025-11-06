# 🤖 Como Configurar o Google Gemini

## ✅ Implementação Completa

O sistema utiliza **Google Gemini** para respostas inteligentes! 

### 🎯 Estratégia de Respostas

O sistema tenta as fontes nesta ordem:
1. **Google Gemini** (IA principal - obrigatória)
2. **Base Local Humanizada** (se Gemini não estiver disponível)

## 📋 Passo a Passo

### 1. Instalar a Biblioteca

```bash
pip install google-generativeai
```

Ou atualize o `requirements.txt` (já atualizado):
```bash
pip install -r requirements.txt
```

### 2. Obter Chave da API do Gemini

1. Acesse: https://aistudio.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada

### 3. Configurar no `.env`

Adicione a chave ao arquivo `.env` na raiz do projeto:

```env
# Gemini (obrigatório para uso da IA)
GEMINI_API_KEY=sua_chave_gemini_aqui
```

### 4. Reiniciar o Servidor

Após adicionar a chave, reinicie o servidor Flask:

```bash
python backend/app.py
```

## ✅ Verificação

Ao iniciar o servidor, você verá:

```
[GEMINI] ✅ Cliente Gemini inicializado com sucesso
```

Ou:

```
[GEMINI] ⚠️ GEMINI_API_KEY não configurada
```

## 🎯 Vantagens do Gemini

1. **Gratuito** - Cota generosa gratuita
2. **Humanização** - Respostas empáticas e conversacionais
3. **Rápido** - Modelo `gemini-1.5-flash` é muito rápido
4. **Fallback Automático** - Usa base local se Gemini não estiver disponível

## 📊 Logs

O sistema registra qual fonte foi usada:

```
[CHAT] ✅ Resposta gerada pela IA (Gemini)
[CHAT] 📚 Resposta da base local HUMANIZADA
```

## ⚠️ Troubleshooting

### Erro: "Biblioteca não instalada"
```bash
pip install google-generativeai
```

### Erro: "GEMINI_API_KEY não configurada"
- Verifique se adicionou a chave no `.env`
- Reinicie o servidor após adicionar

### Erro: "Quota esgotada"
- O sistema automaticamente usa a base local humanizada
- Considere atualizar seu plano no Google AI Studio

## 🚀 Pronto!

Agora você tem **Google Gemini** configurado com fallback automático para base local! 🎉

