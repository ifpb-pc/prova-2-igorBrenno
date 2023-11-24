def processa_lista(valores):
    pass

def indice_menor(lista):
    pass

def organizar_alturas(lista):
    pass

def ler_valores():
    pass

def formatar_alturas(lista):
    pass

def q1(pessoas = {"Joao": 25, "Maria": 20, "Ana": 30}):
    # lista_oredenada = sorted(pessoas, key=lambda dicionario: dicionario)
    lista = []
    dic = pessoas
    for i in sorted(pessoas, key = lambda dicionario : dicionario):
        if (dic[i] >= 18):
            lista.append(i)
    return(lista)

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    lista = []
    maior = 0
    if len(lista1) > len(lista2): 
        maior = len(lista1)
    else:
        maior = len(lista2)

    for i in range(maior):
        if i < len(lista1):
            lista.append(lista1[i])
        if i < len(lista2):
            lista.append(lista2[i])
    return(lista)

def q3(valores = None):
    #valores = ler_valores()
    # pares, impares = processa_lista(valores)
    # return pares, impares
    valor = []
    while True:
        inp = input()
        if (inp == 0):
            break
        else:
            valor.append(inp)
    print(valor)

def q4(valores = None):
    #valores = ler_valores()
    # lista_ambrosina = organizar_alturas(valores)
    # return formatar_alturas(lista_ambrosina)
    pass






def main():
    pass
    

if __name__ == "__main__":
    main()


