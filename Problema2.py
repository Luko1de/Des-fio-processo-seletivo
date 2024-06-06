"""Para encontrar a nota fiscal faltante é necessário somar todos os números de 1 até N,
onde N é a quantidade total de notas fiscais. Em seguida, somar todas as identificações das notas fiscais presentes.
A diferença entre a soma total e a soma das identificações presentes é a nota fiscal faltante."""

def encontrar_nota(arquivo_txt):
    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        N = int(file.readline().strip())
        identificacoes_presentes = list(map(int, file.readline().strip().split()))
    #Usando a formula de PA para encontrar a soma total
    soma_total = N * (N + 1) // 2
    soma_presentes = sum(identificacoes_presentes)
    nota_faltante = soma_total - soma_presentes
    return nota_faltante

arquivo_txt= 'notas.txt'
nota_faltante = encontrar_nota(arquivo_txt)
print(nota_faltante)




