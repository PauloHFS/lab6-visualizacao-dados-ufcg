import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Results.csv')

# Filtrar registros onde constructorId = 1 e position = 1
filtered_df = df[(df['constructorId'] == 6) & (df['position'] == '1')]

# Verificar o número de registros retornados
print(f"Número de registros encontrados: {len(filtered_df)}")

# Salvar o dataframe filtrado em um novo arquivo CSV
filtered_df.to_csv('./Filtered_Sprint_Race_Results.csv', index=False)

