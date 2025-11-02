# 📋 Tarefas Pendentes - Assistente Puerpério

## 🔍 **Status Atual:**

### ✅ **100% Completo:**
1. ✅ Base de conhecimento (79 perguntas)
2. ✅ Telefones úteis integrados
3. ✅ Guias práticos (7 guias)
4. ✅ Cuidados gestação (3 trimestres)
5. ✅ Cuidados pós-parto (4 períodos)
6. ✅ Carteira de vacinação (mãe + bebê)
7. ✅ Nome Sophia implementado
8. ✅ Responsividade proporcional
9. ✅ Visual aconchegante
10. ✅ IA conversacional
11. ✅ Mobile otimizado

---

## ⏳ **TAREFAS FALTANDO:**

### **1. 🎨 IMAGENS DOS GUIAS PRÁTICOS**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🔴 ALTA

**O que falta:**
- [ ] Adicionar 35-40 imagens aos guias práticos
- [ ] Decidir: URLs externas ou hospedar localmente
- [ ] Criar estrutura de pastas `static/images/guias/`
- [ ] Integrar imagens no frontend
- [ ] Testar exibição

**Documentação:** `COMO_ADICIONAR_IMAGENS.md` criada  
**Próximo passo:** Escolher approach e implementar

---

### **2. 🔐 BACKEND DE AUTENTICAÇÃO**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🔴 MÉDIA

**O que falta:**
- [ ] Criar banco de dados (SQLite inicialmente)
- [ ] Modelo de usuário (nome, email, senha_hash, baby_name, created_at)
- [ ] Hash de senhas com bcrypt
- [ ] Rota `POST /api/register`
- [ ] Rota `POST /api/login`
- [ ] Sessões/cookies (Flask-Login ou JWT)
- [ ] Middleware de autenticação
- [ ] Proteger rotas sensíveis
- [ ] Integrar modal frontend com backend

**Próximo passo:** Implementar db e rotas de auth

---

### **3. 🎨 INTERFACE DE GUIAS NO FRONTEND**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🟡 MÉDIA

**O que falta:**
- [ ] Criar seção "Guias Práticos" visível
- [ ] Cards para cada guia
- [ ] Página/modal detalhado do guia
- [ ] Exibir imagens
- [ ] Navegação entre guias
- [ ] Mobile-friendly

---

### **4. 📅 INTERFACE DE CUIDADOS SEMANAIS**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🟡 MÉDIA

**O que falta:**
- [ ] Criar seção "Meus Cuidados"
- [ ] Seletor de gestação/pós-parto
- [ ] Timeline das semanas
- [ ] Exibir cuidados da semana atual
- [ ] Próximos cuidados
- [ ] Integração com cadastro

---

### **5. 💉 INTERFACE DA CARTEIRA DE VACINAÇÃO**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🟡 BAIXA

**O que falta:**
- [ ] Seção "Minhas Vacinas"
- [ ] Toggle mãe/bebê
- [ ] Calendário visual
- [ ] Marcar como "tomada"
- [ ] Próximas vacinas
- [ ] Histórico

---

### **6. 🎯 MELHORIAS DE INTEGRAÇÃO**
**Status:** ⏳ PENDENTE  
**Prioridade:** 🟢 BAIXA

**O que falta:**
- [ ] Frontend para exibir telefones (fora do chat)
- [ ] Botão "Ligar agora" no modal de alerta
- [ ] Dashboard personalizado por usuário
- [ ] Notificações push
- [ ] Dark mode
- [ ] App PWA

---

### **7. 🐛 BUGS/MELHORIAS CONHECIDOS**
**Status:** ⏳ INVESTIGAÇÃO  
**Prioridade:** 🟡 MÉDIA

**Mencionado pelo usuário:**
- [ ] **Respostas não batem com perguntas** - Investigar
- [ ] Talvez ajustar similaridade (0.7 -> 0.5?)
- [ ] Melhorar search na base local
- [ ] Testar com várias perguntas

---

## 🎯 **Prioridade de Execução:**

### **Fase 1 - Essencial (PRÓXIMOS):**
1. **Imagens dos guias práticos** 🔴 ALTA
2. **Investigar respostas IA** 🔴 ALTA
3. **Backend de autenticação** 🔴 MÉDIA

### **Fase 2 - Importante:**
4. **Interface de guias** 🟡 MÉDIA
5. **Interface cuidados semanais** 🟡 MÉDIA

### **Fase 3 - Nice to Have:**
6. **Interface vacinação** 🟢 BAIXA
7. **Melhorias extras** 🟢 BAIXA

---

## 📊 **Estimativa:**

**Próxima sessão (2-3h):**
- Implementar imagens dos guias
- Investigar/resolver respostas IA
- Iniciar backend de auth

**Sessão seguinte (3-4h):**
- Completar backend de auth
- Criar interfaces de guias e cuidados
- Testar tudo junto

**Futuro:**
- Interface vacinação
- Melhorias de UX
- PWA/App

---

## ❓ **DECISÕES PENDENTES:**

1. **Imagens:** URLs externas ou local?
2. **Database:** SQLite agora, PostgreSQL depois?
3. **Auth:** Flask-Login ou JWT?
4. **Deploy:** Render OK ou migrar?

---

**Status Geral:** ✅ **85% Completo** - Falta implementar frontends e auth

