# 📊 Análise de Gastos Familiares

Este projeto é um exemplo prático de como utilizar a biblioteca **Pandas** em Python para **converter, limpar e analisar dados financeiros**.  
O objetivo é transformar dados brutos de gastos familiares em **insights úteis**, destacando as áreas com maior potencial de economia.

---

## 🚀 Funcionalidades

O script **`analise_gastos.py`** realiza as seguintes etapas:

- **Conversão de Arquivos:**  
  Lê dados de uma planilha `.xlsx` e converte-os para o formato `.csv`.

- **Transformação de Dados:**  
  Reorganiza os dados de forma eficiente para a análise, utilizando a função `melt()` do Pandas para transformar categorias em linhas.

- **Análise Financeira:**  
  - Calcula o **gasto médio anual da família**.  
  - Identifica as **categorias de gastos mais altas**, mostrando onde o dinheiro está sendo mais gasto.

- **Relatório Simples:**  
  Gera um **resumo conciso** com as principais conclusões, como as **top 3 categorias de gastos**, facilitando a visualização dos resultados.

---

## 🛠️ Como Usar

### 1. Pré-requisitos
- **Python 3.x** instalado  
- Bibliotecas: `pandas` e `openpyxl`

### 2. Instalação das dependências
```bash
pip install pandas openpyxl

