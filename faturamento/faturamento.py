import json

# Função para calcular os dados
def calcular_faturamento(faturamento_diario):
    # Filtra os dias com faturamento (ignora dias com faturamento 0)
    faturamento_valido = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]
    
    # Calcula o menor e maior valor de faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    
    # Calcula a média mensal
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    # Conta os dias com faturamento acima da média
    dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carrega os dados do JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados["faturamento_diario"]

# Chama a função e obtém os resultados
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

# Exibe os resultados
print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
