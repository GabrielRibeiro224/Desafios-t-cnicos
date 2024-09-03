# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcula e imprime o percentual de representação de cada estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado} – {percentual:.2f}%")

# Se rodar o código com os dados que foram fornecidos, o resultado será esse: 

# SP – 37.53%
# RJ – 20.29%
# MG – 16.17%
# ES – 15.03%
# Outros – 10.98%
