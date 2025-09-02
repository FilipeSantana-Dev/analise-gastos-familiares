import pandas as pd

# 1. Importar arquivo XLSX
df = pd.read_excel("Gastos_Familiares_5_anos.xlsx")

# 2. Converter para CSV
arquivo_csv = 'gastos_familia.csv'
df.to_csv(arquivo_csv, index=False)
print(f'Arquivo convertido para CSV: {arquivo_csv}')

# 3. Exibir as primeiras linhas
print('\nPrimeiras linhas dos dados:')
print(df.head())

# 4. Transformar dados: de colunas de categorias para linhas
df_melt = df.reset_index().melt(id_vars="Ano", var_name="Categoria", value_name="Valor")

# 5. Análise: Gasto médio anual
gasto_anual = df_melt.groupby("Ano")["Valor"].sum()
media_anual = gasto_anual.mean()
print(f'\nGasto médio anual: R$ {media_anual:.2f}')

# 6. Análise
gastos_categoria = df_melt.groupby("Categoria")["Valor"].sum().sort_values(ascending=False)
print('\nGastos totais por categoria:')
print(gastos_categoria)

# 7. Sugestão de economia
print('\nÁreas onde pode economizar (top 3 categorias):')
print(gastos_categoria.head(3))

# 8. Relatório simples
print('\nResumo do relatório:')
print(f'- Gasto médio anual: R$ {media_anual:.2f}')
print('- Top 3 categorias de gasto:')
for categoria, valor in gastos_categoria.head(3).items():
    print(f'  {categoria}: R$ {valor:.2f}')
