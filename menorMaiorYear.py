import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Schedule.csv')

# Pegar o maior e menor ano (year)
maior_ano = df['year'].max()
menor_ano = df['year'].min()

# Exibir os resultados
print(f"Maior ano: {maior_ano}") # = 2024
print(f"Menor ano: {menor_ano}") # = 1950
