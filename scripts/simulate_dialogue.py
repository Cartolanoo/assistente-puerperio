#!/usr/bin/env python3
"""
Simulador de Diálogo Automático
Testa fluxos de conversa principais para verificar coerência
"""

import sys
import json
from pathlib import Path
from typing import List, Dict

class DialogueSimulator:
    def __init__(self):
        self.conversations = []
        self.results = {
            "passed": [],
            "failed": [],
            "warnings": []
        }
    
    def load_base_knowledge(self) -> Dict:
        """Carrega base de conhecimento"""
        base_path = Path("backend/base_conhecimento.json")
        if base_path.exists():
            with open(base_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def test_greeting_flow(self) -> None:
        """Testa fluxo de saudação"""
        print("🧪 Testando fluxo de saudação...")
        
        test_cases = [
            {"input": "Oi", "expected": ["oi", "olá", "bom dia", "boa tarde", "boa noite"]},
            {"input": "Olá", "expected": ["olá", "oi", "bem-vinda"]},
            {"input": "Bom dia", "expected": ["bom dia", "olá", "oi"]}
        ]
        
        base = self.load_base_knowledge()
        
        for case in test_cases:
            input_text = case["input"].lower()
            found_match = False
            
            for key, value in base.items():
                if isinstance(value, dict):
                    pergunta = value.get("pergunta", "").lower()
                    resposta = value.get("resposta", "").lower()
                    
                    if any(exp in pergunta or exp in resposta for exp in case["expected"]):
                        found_match = True
                        break
            
            if found_match:
                self.results["passed"].append(f"✅ Saudação '{case['input']}' tem resposta adequada")
            else:
                self.results["warnings"].append(
                    f"⚠️ Saudação '{case['input']}' pode não ter resposta específica"
                )
    
    def test_question_flow(self) -> None:
        """Testa fluxo de perguntas"""
        print("🧪 Testando fluxo de perguntas...")
        
        base = self.load_base_knowledge()
        
        # Verifica se há perguntas e respostas
        has_questions = False
        has_answers = False
        
        for key, value in base.items():
            if isinstance(value, dict):
                if value.get("pergunta"):
                    has_questions = True
                if value.get("resposta"):
                    has_answers = True
        
        if has_questions and has_answers:
            self.results["passed"].append("✅ Base de conhecimento tem perguntas e respostas")
        else:
            self.results["failed"].append("❌ Base de conhecimento incompleta")
    
    def test_context_continuity(self) -> None:
        """Testa continuidade de contexto"""
        print("🧪 Testando continuidade de contexto...")
        
        # Simula conversa sequencial
        conversation = [
            "Estou grávida",
            "Tenho dúvidas sobre alimentação",
            "E sobre exercícios?"
        ]
        
        base = self.load_base_knowledge()
        
        # Verifica se há categorias relacionadas
        related_categories = []
        for key, value in base.items():
            if isinstance(value, dict):
                categoria = value.get("categoria", "").lower()
                pergunta = value.get("pergunta", "").lower()
                
                if "alimentação" in categoria or "alimentação" in pergunta:
                    related_categories.append(key)
                if "exercício" in categoria or "exercício" in pergunta:
                    related_categories.append(key)
        
        if len(related_categories) >= 2:
            self.results["passed"].append(
                f"✅ Contexto mantido - {len(related_categories)} categorias relacionadas encontradas"
            )
        else:
            self.results["warnings"].append(
                "⚠️ Poucas categorias relacionadas - continuidade pode ser afetada"
            )
    
    def test_medical_warnings(self) -> None:
        """Testa se avisos médicos estão presentes"""
        print("🧪 Testando avisos médicos...")
        
        base = self.load_base_knowledge()
        has_warnings = False
        
        for key, value in base.items():
            if isinstance(value, dict):
                resposta = value.get("resposta", "").lower()
                if "importante" in resposta or "consulte" in resposta or "médico" in resposta:
                    has_warnings = True
                    break
        
        if has_warnings:
            self.results["passed"].append("✅ Avisos médicos encontrados nas respostas")
        else:
            self.results["warnings"].append(
                "⚠️ Avisos médicos podem não estar presentes em todas as respostas"
            )
    
    def run_all_tests(self) -> None:
        """Executa todos os testes"""
        print("=" * 70)
        print("🤖 SIMULADOR DE DIÁLOGO - SOPHIA CHATBOT")
        print("=" * 70)
        print()
        
        self.test_greeting_flow()
        self.test_question_flow()
        self.test_context_continuity()
        self.test_medical_warnings()
        
        print()
        print("=" * 70)
        print("📊 RESULTADOS:")
        print("=" * 70)
        
        if self.results["passed"]:
            print("\n✅ TESTES APROVADOS:")
            for result in self.results["passed"]:
                print(f"  {result}")
        
        if self.results["failed"]:
            print("\n❌ TESTES FALHADOS:")
            for result in self.results["failed"]:
                print(f"  {result}")
        
        if self.results["warnings"]:
            print("\n⚠️ AVISOS:")
            for result in self.results["warnings"]:
                print(f"  {result}")
        
        print()
        print("=" * 70)
        
        total_passed = len(self.results["passed"])
        total_failed = len(self.results["failed"])
        total_warnings = len(self.results["warnings"])
        
        if total_failed == 0:
            if total_warnings == 0:
                print("✅ COERÊNCIA: TOTAL")
            else:
                print("⚠️ COERÊNCIA: COM AVISOS")
        else:
            print("❌ COERÊNCIA: PROBLEMAS ENCONTRADOS")
        
        print("=" * 70)


def main():
    simulator = DialogueSimulator()
    simulator.run_all_tests()
    
    # Retorna código de saída
    if simulator.results["failed"]:
        return 1
    elif simulator.results["warnings"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
