"""Nesse Código a logica utilizado foi a comparação entre todas as repetições, a contagem de cada uma e sua soma, para disso retornar
a repetição de maior soma e tambem a quantidade de repetições daquele Número, como a entrada é feita com String com M e separadas por virgulas
tive que fazer um tratamento da entrada para que o código consiga ler as medições, 
"""
def maior_sequencia_soma_repeticoes(medicoes):
    maior_soma = 0
    sequencia_atual = 0
    valor_atual = None
    sequencia_repetida = None
    repeticoes = 0

    for medicao in medicoes:
        if medicao == valor_atual:
            sequencia_atual += int(medicao[:-1])
        else:
            if sequencia_atual > maior_soma:
                maior_soma = sequencia_atual
                sequencia_repetida = valor_atual
                repeticoes = 1
            elif sequencia_atual == maior_soma:
                repeticoes += 1
            sequencia_atual = int(medicao[:-1])
            valor_atual = medicao

    # Verificar se a última sequência é a maior
    if sequencia_atual > maior_soma:
        maior_soma = sequencia_atual
        sequencia_repetida = valor_atual
        repeticoes = 1
    elif sequencia_atual == maior_soma:
        repeticoes += 1
    num_repeticoes = medicoes.count(sequencia_repetida)

    return maior_soma, sequencia_repetida, num_repeticoes

def main():
    with open("medicoes.txt", "r") as file:
        num_medicoes = file.readline().strip()
        medicoes = file.readline().strip().split(", ")
    medicoes = [medicao[:-1] if medicao.endswith('M') else medicao for medicao in medicoes]
    medicoes = [medicao.split(",") for medicao in medicoes]
    medicoes = [item for sublist in medicoes for item in sublist]
    maior_soma, sequencia_repetida, repeticoes = maior_sequencia_soma_repeticoes(medicoes)
    print(f"{num_medicoes} medições com a maior soma de repetições: {maior_soma}")
    print(f"O número {sequencia_repetida} se repete {repeticoes} vezes")

if __name__ == "__main__":
    main()