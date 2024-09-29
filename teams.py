import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Results.csv')

# Filtrar os resultados para contar apenas as vitórias (posição 1)
vitorias_df = df[df['position'] == '1']

# Contar a quantidade de vitórias por constructorId
qtd_vitorias = vitorias_df['constructorId'].value_counts()

# Transformar em um DataFrame
result_df = qtd_vitorias.reset_index()
result_df.columns = ['constructorId', 'qtdVitorias']

# Salvar em um novo arquivo CSV
result_df.to_csv('./qtdVitoriasTeam.csv', index=False)
