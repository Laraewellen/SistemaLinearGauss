# Resolução de Sistemas Lineares pelo Método de Gauss
# O algoritmo resolve sistemas até 4x4 (ou menores)

def gauss_elimination(matrix, n):
    # Etapa 1: Escalonamento (forma triangular superior)
    for i in range(n):
        if matrix[i][i] == 0:
            for k in range(i + 1, n):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
        for j in range(i + 1, n):
            fator = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= fator * matrix[i][k]

    # Etapa 2: Substituição regressiva
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matrix[i][j] * x[j]
        x[i] = (matrix[i][n] - soma) / matrix[i][i]
    return x

# Entrada de dados
n = int(input("Digite o número de variáveis (até 4): "))

matrix = []
print("Digite os coeficientes e o termo independente de cada equação:")
for i in range(n):
    linha = list(map(float, input(f"Equação {i + 1}: ").split()))
    matrix.append(linha)

# Resolução
solucao = gauss_elimination(matrix, n)

# Saída
print("\nSoluções encontradas:")
for i in range(n):
    print(f"x{i + 1} = {solucao[i]:.2f}")
