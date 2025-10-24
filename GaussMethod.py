import tkinter as tk
from tkinter import messagebox, scrolledtext

# Função principal: método de Gauss com pivoteamento parcial
def gauss_elimination(matrix, n, output):
    output.insert(tk.END, "\n=== Início do escalonamento ===\n")
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        if abs(matrix[i][i]) < 1e-9:
            continue
        for j in range(i + 1, n):
            fator = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= fator * matrix[i][k]
        output.insert(tk.END, f"\nMatriz após o passo {i + 1}:\n")
        for linha in matrix:
            output.insert(tk.END, f"{[f'{x:.2f}' for x in linha]}\n")

    sem_solucao = any(all(abs(matrix[i][j]) < 1e-9 for j in range(n)) and abs(matrix[i][n]) > 1e-9 for i in range(n))
    infinitas = any(all(abs(matrix[i][j]) < 1e-9 for j in range(n)) and abs(matrix[i][n]) < 1e-9 for i in range(n))

    if sem_solucao:
        output.insert(tk.END, "\nO sistema não possui solução.\n")
        return False
    if infinitas:
        output.insert(tk.END, "\nO sistema possui infinitas soluções.\n")
        return False

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if abs(matrix[i][i]) < 1e-9:
            x[i] = 0
            continue
        soma = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (matrix[i][n] - soma) / matrix[i][i]

    output.insert(tk.END, "\nSoluções encontradas:\n")
    for i in range(n):
        output.insert(tk.END, f"x{i + 1} = {x[i]:.2f}\n")
    output.insert(tk.END, "\n=== Fim do cálculo ===\n")
    return True


# Controle da interface
def iniciar():
    try:
        global n, equacoes, etapa
        n = int(entry_n.get())
        if n < 1 or n > 4:
            messagebox.showerror("Erro", "Digite um número entre 1 e 4.")
            return
        entry_n.config(state="disabled")
        btn_iniciar.config(state="disabled")
        btn_novo.pack_forget()

        # 🔹 Mostra instrução ANTES das equações
        label_instrucao.config(
            text=f"Digite os coeficientes e o termo independente de cada equação ({n}x{n}).\nExemplo: 2 1 -1 8"
        )
        label_instrucao.pack(pady=5)

        # 🔹 Depois mostra o campo das equações
        etapa = 1
        equacoes = []
        label_eq.config(text=f"Equação {etapa}:")
        frame_eq.pack(before=label_saida, pady=8)
        label_eq.pack()
        entry_eq.pack(pady=3)
        btn_proximo.pack()
    except:
        messagebox.showerror("Erro", "Digite um número válido de variáveis.")


def proxima_equacao():
    global etapa
    texto = entry_eq.get().strip()
    if not texto:
        messagebox.showwarning("Atenção", "Digite os coeficientes e o termo independente.")
        return
    try:
        linha = list(map(float, texto.split()))
        if len(linha) != n + 1:
            messagebox.showerror("Erro", f"Cada equação deve ter {n + 1} números (coeficientes + termo independente).")
            return
        equacoes.append(linha)
        entry_eq.delete(0, tk.END)
        if etapa < n:
            etapa += 1
            label_eq.config(text=f"Equação {etapa}:")
        else:
            frame_eq.pack_forget()
            btn_resolver.pack(pady=10)
    except:
        messagebox.showerror("Erro", "Entrada inválida. Digite números separados por espaço.")


def resolver():
    output.delete("1.0", tk.END)
    btn_resolver.pack_forget()
    resultado = gauss_elimination(equacoes, n, output)

    # Mostra o botão de novo sistema SEMPRE, mesmo se não houver solução
    output.insert(tk.END, "\n-------------------------------\n")
    output.insert(tk.END, "Cálculo finalizado.\n")
    btn_novo.pack(pady=10)


def novo_sistema():
    # Reseta todos os campos e volta ao início
    entry_n.config(state="normal")
    entry_n.delete(0, tk.END)
    btn_iniciar.config(state="normal")
    label_instrucao.config(text="")
    output.delete("1.0", tk.END)
    btn_resolver.pack_forget()
    btn_novo.pack_forget()


# Configuração da janela principal
janela = tk.Tk()
janela.title("Resolução de Sistemas Lineares (Método de Gauss)")
janela.geometry("640x700")
janela.configure(bg="#f4f4f8")

# Cabeçalho
tk.Label(janela, text="Digite o número de variáveis (até 4):", bg="#f4f4f8", font=("Arial", 10, "bold")).pack(pady=5)
entry_n = tk.Entry(janela, width=10, font=("Arial", 10))
entry_n.pack()
btn_iniciar = tk.Button(janela, text="Iniciar", command=iniciar, bg="#6A0DAD", fg="white",
                        font=("Arial", 10, "bold"), width=10)
btn_iniciar.pack(pady=5)

# 🔹 Label de instrução
label_instrucao = tk.Label(janela, text="", bg="#f4f4f8", font=("Arial", 10), fg="gray")

# 🔹 Campo das equações 
frame_eq = tk.Frame(janela, bg="#f4f4f8")
label_eq = tk.Label(frame_eq, text="", bg="#f4f4f8", font=("Arial", 10, "bold"))
entry_eq = tk.Entry(frame_eq, width=30, font=("Courier New", 10))
btn_proximo = tk.Button(frame_eq, text="Próxima", command=proxima_equacao, bg="#9370DB", fg="white",
                        font=("Arial", 9, "bold"), width=10)

# 🔹 Label de saída
label_saida = tk.Label(janela, text="Saída (passos e resultados):", bg="#f4f4f8", font=("Arial", 10, "bold"))
label_saida.pack(pady=5)

# 🔹 Área de saída (terminal visual)
output = scrolledtext.ScrolledText(janela, width=75, height=20, font=("Courier New", 10),
                                   bg="#1e1e1e", fg="#00FF00")
output.pack(pady=5)

# 🔹 Botões inferiores
btn_resolver = tk.Button(janela, text="Resolver", command=resolver, bg="#6A0DAD", fg="white",
                         font=("Arial", 10, "bold"), width=15)
btn_novo = tk.Button(janela, text="Novo Sistema", command=novo_sistema, bg="#444444", fg="white",
                     font=("Arial", 10, "bold"), width=15)

janela.mainloop()
