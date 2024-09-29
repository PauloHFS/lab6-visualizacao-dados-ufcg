# # import pandas as pd

# # # Carregar o arquivo CSV
# # df = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Schedule.csv')

# # # Filtrar os raceId menores que 1233
# # filtered_df = df[df['raceId'] < 1233]

# # # Agrupar por 'year' e transformar em um dicionário {year: List<raceId>}
# # race_dict = filtered_df.groupby('year')['raceId'].apply(list).to_dict()

# # # Exibir o dicionário
# # print(race_dict)


# # # agora preciso do seguinte: uma estrutura de dados do tipo { constructorId: {anox: int, anoy: int, anoz: z ...} } para cada ano em race_dict.
# # # para cada item em constructorsId, você montará um dicionário contendo o somátorio de todas as corridas ganhas pelo time.
# # # Para isso, você deverá ver todas as corridas com id em racesId e irá fazer o somatório 




# import pandas as pd

# # Carregar os arquivos CSV
# df_schedule = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Schedule.csv')
# df_results = pd.read_csv('/home/gabriel.dantas.oliveira/Downloads/Formula 1 World Championship History (1950-2024)(1)/Race_Results.csv')

# constructor_ids = [6, 1, 131, 9, 3, 32, 4, 22, 34, 25]
# # Filtrar os raceId menores que 1233 no 'Race_Schedule'
# filtered_df_schedule = df_schedule[df_schedule['raceId'] < 1233]

# # Criar o dicionário {year: List<raceId>}
# race_dict = filtered_df_schedule.groupby('year')['raceId'].apply(list).to_dict()

# # Criar a estrutura {constructorId: {anoX: int, anoY: int, ...}}
# constructor_victories = {}

# # Percorrer cada ano e os raceId correspondentes no race_dict
# for year, race_ids in race_dict.items():
#     # Filtrar resultados com os raceId correspondentes e posição igual a 1 (vitória)
#     filtered_results = df_results[(df_results['raceId'].isin(race_ids)) & (df_results['positionOrder'] == 1)]
    
#     # Agrupar por constructorId e contar as vitórias por ano
#     victories_per_constructor = filtered_results.groupby('constructorId').size()
    
#     # Atualizar o dicionário constructor_victories
#     for constructor_id, victories in victories_per_constructor.items():
#         if constructor_id not in constructor_victories:
#             constructor_victories[constructor_id] = {}
#         constructor_victories[constructor_id][year] = victories

# # Exibir a estrutura de dados final
# print(constructor_victories)




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

# Exibir a estrutura de dados final
print(constructor_victories)
