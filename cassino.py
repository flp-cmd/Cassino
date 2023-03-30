MAX_APOSTA = 1000  ## APOSTA MÁXIMA
MIN_APOSTA = 10  ## APOSTA MÍNIMA
LINHA = 3  ## NÚMERO DE LINHAS
COLUNAS = 3 ## NÚMERO DE COLUNAS
import random

contagem_simbolos = {"A":3,"B":6,"C":9,"D":12,"E":15} #Símbolos Possíveis e suas quantidades respectivas
contagem_valores = {"A":15,"B":12,"C":9,"D":6,"E":3} #Valores de cada símbolo para cálculo dos ganhos

def get_cassino_roleta(linhas_,colunas_,simbolos): # Função que retorna uma lista de listas sendo cada lista uma linha da matriz
    todos_simbolos = []
    for simbolo,simbolo_cont in simbolos.items():
        for _ in range(simbolo_cont):
            todos_simbolos.append(simbolo)
    
    colunas = []
    for _ in range(colunas_):
        coluna = []
        tempList = todos_simbolos[:]
        for _ in range(linhas_):
            valor = random.choice(tempList)
            tempList.remove(valor)
            coluna.append(valor)
        colunas.append(coluna)

    return colunas

def print_roleta(colunas): # Imprime no console a matriz de simbolos sorteados
    for linha in colunas:
        for simbolo in linha:
            print(f"| {simbolo} ",end="")
        print("|")

def depositar(): #Recebe do usuario um valor a ser depositado e retorna este valor
    while(True):
        qtd = input("Digite quanto quer depositar: R$")
        if qtd.isdigit():
            qtd = int(qtd)
            if qtd > 0:
                break
            else:
                print("Depósitos devem ser acima de 0!")
        else:
            print("Digite um número por favor!")
    return qtd

def qtd_de_linhas(): #Recebe do usuario o numero de linhas que ele quer apostar, retorna este valor
    while(True):
        linhas = input("Em quantas linhas quer apostar(1-"+str(LINHA)+"): ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= LINHA:
                break
            else:
                print("Digite um número de linhas entre 1 e 3 por favor!")
        else:
            print("Digite um número por favor!")
    return linhas

def valor_aposta(): # Recebe do usuario o valor que ele quer apostar em cada linha, retorna este valor
    while(True):
        valor = input("Digite quanto deseja apostar em cada linha: ")
        if valor.isdigit():
            valor = int(valor)
            if MIN_APOSTA <= valor <= MAX_APOSTA:
                break
            else:
                print(f"Digite um valor entre {MIN_APOSTA}R$ e {MAX_APOSTA}R$ por favor!")
        else:
            print("Digite um número por favor!")
    return valor

def checa_ganhos(simbolos,linhas,aposta,valores): #Função que verifica se o usuario ganhou em alguma linha que apostou, calcula os ganhos baseado nos valores dos simbolos e o total apostado, retorna os ganhos e as linhas em que o usuario ganhou
    ganhos = 0
    linhas_ganhas = []
    simbolos_acertados = []
    for linha in range(linhas):
        if simbolos[linha][0] == simbolos[linha][1] == simbolos[linha][2]:
            ganhos += valores[simbolos[linha][0]] * aposta
            linhas_ganhas.append(linha + 1)
            simbolos_acertados.append(simbolos[linha][0])
    return ganhos, linhas_ganhas, simbolos_acertados

def roleta(caixa): #Funcao que chama as outras, retorna o saldo da aposta
    resultado = get_cassino_roleta(LINHA,COLUNAS,contagem_simbolos)
    while(True):
        linhas = qtd_de_linhas()
        aposta = valor_aposta()
        total_aposta = linhas * aposta
        if total_aposta > caixa or caixa < 10:
            print(f"Você não tem dinheiro suficiente no caixa para realizar essa aposta, seu caixa atual é de: {caixa}R$ e sua aposta foi de: {total_aposta}R$")
            deposito = input("Digite 'd' se quiser depositar mais dinheiro ou enter para apostar outro valor: ")
            if deposito.lower() == "d":
                caixa += depositar()
                print(f"Seu caixa atual é de {caixa}R$")
        else:
            break

    print(f"Você está apostando {aposta}R$ em {linhas} linhas, seu total apostado é: {total_aposta}R$")
    print_roleta(resultado)
    ganhos,linhas_ganhas,simbolos_acertados = checa_ganhos(resultado,linhas,aposta,contagem_valores)
    if ganhos > 0:
        print(f"Você ganhou {ganhos}R$")
        if len(linhas_ganhas) == 1:
            print("Você venceu na linha",*linhas_ganhas,end="")
            print(" com o simbolo",*simbolos_acertados)
        else:
            print("Você venceu nas linhas:",*linhas_ganhas,end="")
            print(" com os simbolos:",*simbolos_acertados)
    else:
        print("Você não ganhou em nenhuma linha.")

    caixa = caixa + (ganhos - total_aposta)
    return caixa

def main(): # Função principal que armazena o caixa do usuario e chama a roleta
    caixa =  depositar()
    caixa = roleta(caixa)
    while(True):
        print(f"Seu caixa atual é de {caixa}R$")
        if  caixa < 10:
            print(f"Você não tem dinheiro suficiente no caixa para apostar, seu caixa atual é de: {caixa}R$")
            deposito = input("Digite 'd' se quiser depositar mais dinheiro ou 's' para sair: ")
            if deposito.lower() == "d":
                caixa += depositar()
                print(f"Seu caixa atual é de {caixa}R$")
            elif deposito.lower() == "s":
                break
        repetir = input("Aperte enter para jogar novamente, 'd' para depositar mais dinheiro ou 's' para sair: ")
        if repetir.lower() == "s":
            break
        elif repetir.lower() == "d":
            caixa += depositar()
        elif repetir.lower() == "":
            caixa = roleta(caixa)

    print(f"Você saiu com {caixa}R$")
main()