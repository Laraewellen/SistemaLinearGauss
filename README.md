<p align="center">
  <img src="https://img.shields.io/badge/🧮%20Álgebra%20Linear%20-%20Método%20de%20Gauss%20com%20Pivoteamento%20Parcial-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF">
</p>

# 💜 Algoritmo de Resolução de Sistemas Lineares (Método de Gauss com Pivoteamento Parcial)

Este projeto foi desenvolvido como atividade prática da disciplina **Álgebra Linear**, com o objetivo de implementar um **algoritmo capaz de resolver sistemas lineares** (de 1x1 até 4x4) **utilizando o método de Eliminação de Gauss com Pivoteamento Parcial**, sem o uso de bibliotecas prontas.

O diferencial do projeto é a **interface gráfica em Tkinter**, que torna o processo visual, mostrando **cada etapa do escalonamento da matriz** e os resultados passo a passo.  
Além disso, o programa identifica automaticamente **sistemas sem solução** e **sistemas com infinitas soluções**.

---

![🚀 Funcionalidades](https://img.shields.io/badge/🚀%20Funcionalidades-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

- Interface visual desenvolvida com **Tkinter**  
- Resolução de sistemas de até **4 equações e 4 incógnitas**  
- **Pivoteamento Parcial** para maior estabilidade numérica  
- Exibição da **matriz a cada passo** do escalonamento  
- Detecção de **sistemas sem solução** e **infinitas soluções**  
- Botão **“Novo Sistema”** para resolver diferentes casos sem reiniciar o programa  

---

![⚙️ Tecnologias Utilizadas](https://img.shields.io/badge/⚙️%20Tecnologias%20Utilizadas-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

- **Python 3**
- **Tkinter (biblioteca padrão)**

---

![📘 Método Utilizado](https://img.shields.io/badge/📘%20Método%20Utilizado-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

O método de **Eliminação de Gauss com Pivoteamento Parcial** transforma a matriz aumentada do sistema em uma **matriz triangular superior**, permitindo resolver as incógnitas por **substituição regressiva**.  
O pivoteamento parcial escolhe o maior valor absoluto da coluna para reduzir erros numéricos e evitar divisões por zero.  
Durante o processo, o programa exibe o estado da matriz após cada passo, facilitando o entendimento didático.

---

![🧭 Passo a Passo de Utilização](https://img.shields.io/badge/🧭%20Passo%20a%20Passo%20de%20Utilização-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

Abaixo estão as etapas que o usuário segue ao utilizar o programa:

| Etapa | Descrição | Imagem |
|:--:|:--|:--:|
| **1** | Abra o programa e insira o número de variáveis. | ![1 - digitando vetor](imgs/1-%20digitando%20vetor.png) |
| **2** | Clique em **Iniciar**. | ![2 - iniciando](imgs/2-%20iniciando.png) |
| **3** | O campo para inserir a **1ª equação** será exibido. | ![3 - campo para inserir a 1ª equação](imgs/3-%20campo%20para%20inserir%20a%201ª%20equação.png) |
| **4** | Leia a **instrução** e siga o exemplo mostrado. | ![4 - instrução](imgs/4%20-%20instrução.png) |
| **5** | Digite a equação e clique em **Próxima**. | ![5 - insira a equação e clique em próxima](imgs/5-%20insira%20a%20equação%20e%20clique%20em%20proxima.png) |
| **6** | Continue inserindo as equações até terminar. | ![6 - insira a outra equação e clique em próxima até acabar](imgs/6-%20insira%20a%20outra%20equação%20e%20clique%20em%20próxima,%20até%20acabar.png) |
| **7** | Após inserir todas, aparecerá o botão **Resolver**. | ![7 - assim que terminar de inserir aparecerá o botão enviar](imgs/7-%20assim%20que%20terminar%20de%20inserir%20aparecerá%20o%20botão%20enviar.png) |
| **8** | Veja o **resultado do escalonamento**. | ![8 - resultado](imgs/8-%20resultado.png) |
| **9** | O programa exibe a **continuação do resultado** e as soluções. | ![9 - continuação do resultado](imgs/9-%20continuação%20do%20resultado.png) |
| **10** | Caso o sistema **não possua solução**, será informado. | ![10 - o sistema não possui solução](imgs/10-%20o%20sistema%20não%20possui%20solução.png) |
| **11** | Caso o sistema **possua infinitas soluções**, também será exibido. | ![11 - o sistema possui infinitas soluções](imgs/11-%20o%20sistema%20possui%20infinitas%20soluções.png) |
| **12** | Clique em **Novo Sistema** para resolver outro caso. | ![12 - clique em novo sistema](imgs/12-%20clique%20em%20novo%20sistema.png) |
| **13** | Repita o processo quantas vezes desejar. | ![13 - repita](imgs/13-%20repita.png) |

---

![💡 Exemplos de Entrada](https://img.shields.io/badge/💡%20Exemplos%20de%20Entrada-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

### Sistema 2x2
```
2x + y = 8
x - 4y = -2
```
Entrada no programa:
```
2 1 8
1 -4 -2
```

### Sistema 3x3
```
x + y + z = 6
2x - y + z = 3
x - 2y + 3z = 14
```
Entrada no programa:
```
1 1 1 6
2 -1 1 3
1 -2 3 14
```

---

![👩‍💻 Autoras](https://img.shields.io/badge/👩‍💻%20Autoras-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

👩‍💻 **Lara Ewellen de Carvalho Rocha**  
👩‍💻 **Júlia Gabriela Gomes da Silva**

---


![📄 Documentação Completa](https://img.shields.io/badge/📄%20Documentação%20Completa-7F3FBF?style=for-the-badge&labelColor=7F3FBF&color=7F3FBF)

Abaixo está a documentação completa do projeto, com introdução teórica, explicação detalhada, código comentado e instruções de uso:

<p align="center">
  <img src="https://github.com/Laraewellen/SistemaLinearGauss/blob/73929b27b0e5e3e6851714ae4124b73b40ddf20a/Algoritmo%20de%20Resolu%C3%A7%C3%A3o%20de%20Sistemas%20Lineares%20pelo%20M%C3%A9todo%20de%20Gauss%20(com%20Pivoteamento%20Parcial)%20Lara%20Ewellen%20e%20J%C3%BAlia%20Gabriela%20Gomes.pdf" width="700">
</p>

---

<p align="center">
  <b> Projeto desenvolvido para fins acadêmicos 💜</b>
</p>
