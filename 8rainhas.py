import time

#Função para saber se as casas do tabuleiros estão livres
def livre(tabuleiro, linha, coluna, n):
    # Verifica a linha à esquerda
    for i in range(coluna):
        if tabuleiro[linha][i] == 1:
            return False
    
    # Verifica a diagonal superior esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False
    
    # Verifica a diagonal inferior esquerda
    for i, j in zip(range(linha, n, 1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False
    
    return True

#Função recursiva que implementa backtracking
def resolvendo_n_rainhas_backtracking(tabuleiro, coluna, n, solucao):
    # Caso base: todas as rainhas foram colocadas
    if coluna >= n:
        # Salva uma cópia da solução
        solucao.append([linha[:] for linha in tabuleiro])
        return
    
    # Tenta colocar a rainha em todas as linhas da coluna atual
    for linha in range(n):
        if livre(tabuleiro, linha, coluna, n):
            # ccolocar a rainha
            tabuleiro[linha][coluna] = 1
            
            # Recursão para a próxima coluna
            resolvendo_n_rainhas_backtracking(tabuleiro, coluna + 1, n, solucao)
            
            # Backtrack: remove a rainha
            tabuleiro[linha][coluna] = 0

def resolvendo_8rainhas():
    n = 8
    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]
    solucao = []
    
    resolvendo_n_rainhas_backtracking(tabuleiro, 0, n, solucao)
    
    return solucao

#Função de criação do tabuleiro no terminal
def print_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    
    print("  " + " ".join(str(i) for i in range(n)))
    print("  " + "-" * (2 * n - 1))
    
    for i in range(n):
        print(f"{i}|", end="")
        for j in range(n):
            if tabuleiro[i][j] == 1:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()

#Função para converter matriz para lista
def lista_de_tabuleiro(tabuleiro):

    n = len(tabuleiro)
    result = [-1] * n
    for linha in range(n):
        for coluna in range(n):
            if tabuleiro[linha][coluna] == 1:
                result[coluna] = linha
    return result

#Função para imprimir todas as soluções
def print_todas_solucoes(solucao):

    n_solucao = len(solucao)
    print(f"\nTotal de soluções encontradas: {n_solucao}")
    
    print("\nTodas as soluções")
    
    solucao_per_linha = 4  # Número de soluções por linha
    for i in range(0, n_solucao, solucao_per_linha):
        for j in range(solucao_per_linha):
            idx = i + j
            if idx < n_solucao:
                board_list = lista_de_tabuleiro(solucao[idx])
                print(f"Solução {idx+1:2d}: {board_list}", end="  ")
        print()


#Função para visualizar uma solução específica
def solução_específica(solucao):
    n_solucao = len(solucao)
    
    print(f"Visualizar problema específico")
    
    while True:
        try:
            choice = int(input(f"\nDigite o número da solução (1-{n_solucao}) ou 0 para voltar: "))
            
            if choice == 0:
                break
            elif 1 <= choice <= n_solucao:
                print(f"\nSolução {choice}:")
                print(f"Representação em lista: {lista_de_tabuleiro(solucao[choice-1])}")
                print("\nTabuleiro:")
                print_tabuleiro(solucao[choice-1])
                
                # Pergunta se quer continuar
                cont = input("\nVer outra solução? (s/n): ")
                if cont.lower() != 's':
                    break
            else:
                print(f"Por favor, digite um número entre 1 e {n_solucao}")
                
        except ValueError:
            print("Entrada inválida! Digite um número.")

def main():

    print("Problema das 8 rainhas - BACKTRACKING")

    start_time = time.time()
    solucao = resolvendo_8rainhas()
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    while True:
        print(f"Tempo para encontrar todas as soluções: {execution_time:.4f} segundos")
        print(f"Total de soluções encontradas: {len(solucao)}")
        
        print("1. Ver todas as soluções (formato compacto)")
        print("2. Visualizar uma solução específica")
        print("3. Ver estatísticas")
        print("4. Sair")
        
        choice = input("\nEscolunaha uma opção (1-4): ")
        
        if choice == "1":
            print_todas_solucoes(solucao)
            
        elif choice == "2":
            solução_específica(solucao)
            
        elif choice == "3":
            print("Estátistica do Problema")

            
            n = len(solucao)
            print(f"Total de soluções: {n}")
            print(f"Tempo de execução: {execution_time:.4f} segundos")
            print(f"Média por solução: {execution_time/n:.6f} segundos")
            
            # Mostra a primeira e última solução
            if n > 0:
                print(f"\nPrimeira solução: {lista_de_tabuleiro(solucao[0])}")
                print(f"Última solução: {lista_de_tabuleiro(solucao[-1])}")
                
            # Calcula algumas estatísticas básicas
            if n > 0:
                # Conta quantas soluções começam com rainha em cada linha da primeira coluna
                start_positions = {}
                for sol in solucao:
                    # Encontra a linha da rainha na primeira coluna
                    for linha in range(8):
                        if sol[linha][0] == 1:
                            start_positions[linha] = start_positions.get(linha, 0) + 1
                            break
                
                print("\nDistribuição das rainhas na primeira coluna:")
                for linha in sorted(start_positions.keys()):
                    count = start_positions[linha]
                    percentage = (count / n) * 100
                    bar = "█" * int(percentage / 5)  # Cada █ representa 5%
                    print(f"  Linha {linha}: {count:2d} soluções ({percentage:5.1f}%) {bar}")
            
        elif choice == "4":
            print("\nObrigado por usar o programa!")
            break
            
        else:
            print("\nOpção inválida! Por favor, escolunaha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()