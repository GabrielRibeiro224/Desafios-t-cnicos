# Função para inverter a string manualmente
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string original do final para o início
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# String de entrada (pode ser alterada ou solicitada ao usuário)
string_original = "Exemplo de string"

# Chama a função para inverter a string
string_invertida = inverter_string(string_original)

# Exibe o resultado
print("String original:", string_original)
print("String invertida:", string_invertida)


# execução das strings em typescript
