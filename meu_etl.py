import pandas as pd

print("--- INICIANDO PROCESSO DE ETL ---")

# ==========================================
# 1. EXTRACT (Extração)
# ==========================================
print("1. Lendo o arquivo original...")
# Aqui o Pandas lê o CSV e transforma em um DataFrame (planilha virtual)
df_vendas = pd.read_csv("vendas_brutas.csv")

# Exibe como os dados estão bagunçados
print("\nDados originais (Com valores nulos e bagunçados):")
print(df_vendas)

# ==========================================
# 2. TRANSFORM (Transformação)
# ==========================================
print("\n2. Transformando e limpando os dados...")

# Limpeza 1: Apagar as linhas onde 'cliente' ou 'produto' estão vazios (NaN)
df_vendas = df_vendas.dropna(subset=['cliente', 'produto'])

# Limpeza 2: Padronizar a coluna 'produto' para deixar tudo em MAIÚSCULO
df_vendas['produto'] = df_vendas['produto'].str.upper()

# Transformação 1: Criar uma nova coluna 'valor_total' (quantidade * preco_unitario)
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

# Exibe como os dados ficaram após a faxina
print("\nDados limpos e calculados:")
print(df_vendas)

# ==========================================
# 3. LOAD (Carga)
# ==========================================
print("\n3. Salvando os dados limpos...")

# Exportar o resultado final para um novo arquivo 'vendas_limpas.csv'
# O index=False evita que o Pandas salve aquela coluna de números 0, 1, 2...
df_vendas.to_csv("vendas_limpas.csv", index=False)

print("--- PROCESSO CONCLUÍDO COM SUCESSO! ---")