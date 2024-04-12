import numpy as np

# Carregando o arquivo CSV
data = np.loadtxt('C:\Users\Samsung\Desktop\ExemploProva\paises.csv', delimiter=',', dtype=str,encoding='utf-8')
#1
# Índices das colunas desejadas
country_idx = 0
region_idx = 1
population_idx = 2
area_idx = 3

# Selecionando apenas as colunas desejadas
sliced_data = data[:, [country_idx, region_idx, population_idx, area_idx]

# Exibindo o resultado
print("Dados dos países:")
print(sliced_data)

#2
# Encontrando as diferentes regiões
regions = sliced_data[:, region_idx]
unique_regions = np.unique(regions)

# Contando o número total de regiões
num_unique_regions = len(unique_regions)

# Mostrando as diferentes regiões
print("As diferentes regiões do planeta são:")
for region in unique_regions:
    print(region)

# Mostrando o número total de regiões
print("Total de regiões únicas:", num_unique_regions)

#3
# Índice da coluna da taxa de alfabetização
alfabetizacao_idx = 9

# Convertendo os dados de taxa de alfabetização para números e calculando a média
taxa_alfabetizacao = data[:, alfabetizacao_idx].astype(float)
media_alfabetizacao = np.mean(taxa_alfabetizacao)

# Exibindo a média da taxa de alfabetização
print("A taxa média de alfabetização do planeta é:", media_alfabetizacao)

#4
# Selecionando apenas os países da América do Norte
paises_norte_america = data[data[:, region_idx] == 'NORTHERN AMERICA']

# Contando o número de países da América do Norte
num_paises_norte_america = len(paises_norte_america)

# Exibindo o resultado
print("O número de países da América do Norte é:", num_paises_norte_america)

#5
gdp_per_capita_idx = 7

# Selecionando apenas os países da América do Sul e do Caribe
paises_latam_caribe = data[data[:, region_idx] == 'LATIN AMER. & CARIB']

# Encontrando o índice do país com a maior renda per capita
max_gdp_per_capita_idx = np.argmax(paises_latam_caribe[:, gdp_per_capita_idx].astype(float))

# Encontrando o país com a maior renda per capita
max_gdp_per_capita_country = paises_latam_caribe[max_gdp_per_capita_idx, country_idx]
max_gdp_per_capita_value = paises_latam_caribe[max_gdp_per_capita_idx, gdp_per_capita_idx]

# Exibindo o resultado
print("O país da América do Sul e do Caribe com a maior renda per capita é:", max_gdp_per_capita_country)
print("Renda per capita:", max_gdp_per_capita_value)