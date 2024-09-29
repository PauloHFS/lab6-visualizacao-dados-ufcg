import pandas as pd

# Carregar os arquivos CSV
df_schedule = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Schedule.csv')
df_results = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Results.csv')

# Lista de constructorIds fornecidos
constructor_ids = [6, 1, 131, 9, 3, 32, 4, 22, 34, 25]

# Filtrar os raceId menores que 1233 no 'Race_Schedule'
filtered_df_schedule = df_schedule[df_schedule['raceId'] < 1233]

# Criar o dicionário {year: List<raceId>}
race_dict = filtered_df_schedule.groupby('year')['raceId'].apply(list).to_dict()

# Criar a estrutura {constructorId: {anoX: int, anoY: int, ...}}
constructor_victories = {constructor_id: {} for constructor_id in constructor_ids}

# Variável para manter contagem acumulada de vitórias
cumulative_victories = {constructor_id: 0 for constructor_id in constructor_ids}

# Percorrer cada ano e os raceId correspondentes no race_dict
for year, race_ids in race_dict.items():
    # Filtrar resultados com os raceId correspondentes, posição igual a 1 (vitória) e constructorIds fornecidos
    filtered_results = df_results[(df_results['raceId'].isin(race_ids)) & 
                                  (df_results['positionOrder'] == 1) & 
                                  (df_results['constructorId'].isin(constructor_ids))]
    
    # Agrupar por constructorId e contar as vitórias por ano
    victories_per_constructor = filtered_results.groupby('constructorId').size()
    
    # Atualizar o dicionário constructor_victories com contagem incremental
    for constructor_id in constructor_ids:
        # Verificar se o construtor teve vitórias nesse ano
        victories = victories_per_constructor.get(constructor_id, 0)
        
        # Incrementar o total acumulado de vitórias
        cumulative_victories[constructor_id] += victories
        
        # Atualizar o dicionário para o ano correspondente
        constructor_victories[constructor_id][year] = cumulative_victories[constructor_id]

# Criar um DataFrame onde cada linha representa um constructorId
df_victories = pd.DataFrame.from_dict(constructor_victories, orient='index').fillna(0).astype(int)

# Renomear as colunas para incluir o ano
df_victories.columns = [f"year_{year}" for year in df_victories.columns]

# Adicionar a coluna constructorId
df_victories['constructorId'] = df_victories.index

# Reorganizar as colunas para ter constructorId à frente
df_victories = df_victories[['constructorId'] + [col for col in df_victories.columns if col != 'constructorId']]

# Salvar o DataFrame em um arquivo CSV
df_victories.to_csv('./constructor_victories.csv', index=False)

# Exibir a estrutura de dados final
print(df_victories)
