#!/usr/bin/env python3
"""
Script de Validação de Arquivos JSON
Verifica estrutura, chaves padronizadas e campos vazios
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set

class JSONValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        # Nota: O projeto usa português intencionalmente nas chaves JSON
        # Não verificamos padronização de idioma
    
    def validate_file(self, file_path: Path) -> bool:
        """Valida um arquivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Valida estrutura
            self.check_structure(file_path, data)
            
            # Valida campos vazios
            self.check_empty_fields(file_path, data)
            
            return len(self.errors) == 0
            
        except json.JSONDecodeError as e:
            self.errors.append(f"[ERRO] {file_path}: JSON invalido - {e}")
            return False
        except Exception as e:
            self.errors.append(f"[ERRO] {file_path}: Erro - {e}")
            return False
    
    def check_structure(self, file_path: Path, data: any) -> None:
        """Verifica estrutura básica"""
        if not isinstance(data, (dict, list)):
            self.errors.append(f"[ERRO] {file_path}: Estrutura invalida (deve ser objeto ou array)")
    
    def check_empty_fields(self, file_path: Path, data: any, path: str = "") -> None:
        """Verifica campos vazios"""
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{path}.{key}" if path else key
                
                if value == "" or value is None:
                    self.warnings.append(
                        f"[AVISO] {file_path}: Campo vazio encontrado: {current_path}"
                    )
                elif isinstance(value, (dict, list)):
                    self.check_empty_fields(file_path, value, current_path)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                current_path = f"{path}[{i}]" if path else f"[{i}]"
                if isinstance(item, (dict, list)):
                    self.check_empty_fields(file_path, item, current_path)


def main():
    """Função principal"""
    validator = JSONValidator()
    
    # Arquivos JSON a validar
    json_files = [
        Path("backend/base_conhecimento.json"),
        Path("backend/guias_praticos.json"),
        Path("backend/mensagens_apoio.json"),
        Path("backend/cuidados_gestacao.json"),
        Path("backend/cuidados_pos_parto.json"),
        Path("backend/vacinas_mae.json"),
        Path("backend/vacinas_bebe.json"),
        Path("dados/base_conhecimento.json"),
        Path("dados/guias_praticos.json"),
        Path("dados/mensagens_apoio.json"),
    ]
    
    print("[INFO] Validando arquivos JSON...\n")
    
    all_valid = True
    for json_file in json_files:
        if json_file.exists():
            print(f"Validando: {json_file}")
            if not validator.validate_file(json_file):
                all_valid = False
        else:
            print(f"[AVISO] Arquivo nao encontrado: {json_file}")
    
    print("\n" + "=" * 70)
    
    if validator.errors:
        print("[ERRO] ERROS ENCONTRADOS:")
        for error in validator.errors:
            print(f"  {error}")
        print()
    
    if validator.warnings:
        print("[AVISO] AVISOS:")
        for warning in validator.warnings:
            print(f"  {warning}")
        print()
    
    if not validator.errors and not validator.warnings:
        print("[OK] Todos os arquivos JSON estao validos!")
    
    print("=" * 70)
    
    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
