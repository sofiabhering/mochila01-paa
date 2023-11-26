# Método estratégia gulosa
def mochila_gulosa(capacidade, pesos, valores):
    # Calcula o valor por unidade de peso para cada item
    valor_por_peso = [(valores[i] / pesos[i], pesos[i], valores[i], i) for i in range(len(pesos))]

    # Ordena os itens em ordem decrescente de valor por unidade de peso
    valor_por_peso.sort(reverse=True)

    mochila = [0] * len(pesos)
    capacidade_restante = capacidade
    valor_total = 0

    # Adiciona itens à mochila na ordem classificada
    for item in valor_por_peso:
        peso = item[1]
        valor = item[2]
        indice = item[3]

        # Verifica se o item cabe na mochila
        if peso <= capacidade_restante:
            mochila[indice] = 1
            capacidade_restante -= peso
            valor_total += valor

    return mochila, valor_total

# Método programação dinâmica
def mochila_01(capacidade, pesos, valores, n):
    # Inicialize uma matriz para armazenar os resultados intermediários
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preencha a matriz usando programação dinâmica
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            # Se o peso do item atual for menor ou igual à capacidade atual
            if pesos[i - 1] <= w:
                # Escolha o máximo entre incluir ou não incluir o item
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                # Se o peso for maior que a capacidade, não inclua o item
                dp[i][w] = dp[i - 1][w]

    # O valor máximo estará na célula inferior direita da matriz
    return dp[n][capacidade]

# Menu de escolha
print("Escolha o método:")
print("1. Estratégia Gulosa")
print("2. Programação Dinâmica")

opcao = input("Digite o número correspondente ao método desejado: ")

# Exemplo de uso com base na opção escolhida
capacidade_mochila = 10
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
numero_itens = len(pesos)

if opcao == "1":
    mochila, valor_total = mochila_gulosa(capacidade_mochila, pesos, valores)
    print("Método Guloso:")
    print("Itens na mochila:", mochila)
    print("Valor total na mochila:", valor_total)

elif opcao == "2":
    resultado = mochila_01(capacidade_mochila, pesos, valores, numero_itens)
    print("Método de Programação Dinâmica:")
    print("Itens na mochila:", capacidade_mochila)
    print("Valor total da mochila:", resultado)

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
