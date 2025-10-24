# Resolução de Sistemas Lineares pelo Método de Gauss com Pivoteamento Parcial
# Exibe a matriz após cada passo e detecta sistemas sem solução ou infinitas soluções

def gauss_elimination(matrix, n):
    # Etapa 1: Escalonamento com pivoteamento parcial
    for i in range(n):
        # Pivoteamento parcial: encontra o maior valor absoluto na coluna i
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Troca de linhas se necessário
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Se o pivô for zero, pula a eliminação (tratará depois)
        if abs(matrix[i][i]) < 1e-9:
            continue

        # Zera os elementos abaixo do pivô
        for j in range(i + 1, n):
            fator = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= fator * matrix[i][k]

        # Exibe a matriz após cada passo
        print(f"\nMatriz após o passo {i + 1}:")
        for linha in matrix:
            print(["{:.2f}".format(x) for x in linha])

    # Verifica linhas que indicam sistema impossível ou indeterminado
    sem_solucao = False
    infinitas = False
    for i in range(n):
        if all(abs(matrix[i][j]) < 1e-9 for j in range(n)) and abs(matrix[i][n]) > 1e-9:
            sem_solucao = True
        if all(abs(matrix[i][j]) < 1e-9 for j in range(n)) and abs(matrix[i][n]) < 1e-9:
            infinitas = True

    if sem_solucao:
        print("\nO sistema não possui solução.")
        return None
    if infinitas:
        print("\nO sistema possui infinitas soluções.")
        return None

    # Etapa 2: Substituição regressiva
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if abs(matrix[i][i]) < 1e-9:
            x[i] = 0
            continue
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
    if len(linha) != n + 1:
        print(f"Erro: você deve digitar {n + 1} números por linha.")
        exit()
    matrix.append(linha)

# Resolução
solucao = gauss_elimination(matrix, n)

# Saída
if solucao:
    print("\nSoluções encontradas:")
    for i in range(n):
        print(f"x{i + 1} = {solucao[i]:.2f}")
