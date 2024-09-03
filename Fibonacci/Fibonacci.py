def is_fibonacci(n):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se o número informado é 0 ou 1, que são os dois primeiros números da sequência
    if n == 0 or n == 1:
        return True
    
    # Gera os próximos números da sequência até que o valor seja igual ou maior que n
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número informado é igual ao número atual da sequência
    return b == n

# Solicita ao usuário que informe um número
num = int(input("Informe um número: "))

# Verifica se o número informado pertence à sequência de Fibonacci
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

# Exemplo de execução: 

# Se o usuário informar 13, o programa retornará: O número 13 pertence à sequência de Fibonacci.

# Se o usuário informar 14, o programa retornará: O número 14 NÃO pertence à sequência de Fibonacci.