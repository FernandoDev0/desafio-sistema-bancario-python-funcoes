def menuUsuario():
    menu = """
        ======= Menu ==========
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar Contas
        [nu] Novo Usuario
        [q] Sair            
        """
    return menu


def extratao(saldo, extrato ):
    return f"\nSaldo: R$ {saldo:.2f}\n{extrato} \n" 


def sacar(valor,saldo,limite_maximo,limite_saques,numero_saques,extrato):

    
    limite_saldo = valor > saldo
    limite_maximo = valor > limite_maximo
    limite_saques = numero_saques >= limite_saques

    if limite_saldo:
        print("saldo insuficiente...")
    elif limite_maximo:
        print("o valor do salque passou do limite permitido")
    elif limite_saques:
        print("ops so pode fazer 3 saques por dia, volte amanha")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        numero_saques += 1 
        print("\nSaque Realizado!\n ")
    else:
        print("operacao falhou !  O valor informado é invalido .")

    return valor,saldo,extrato,numero_saques
    

def depositar(valor,saldo,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de RS {valor:.2f}\n"
        print("\nDeposito Realizado com Sucesso !\n")
    else:
        print("operacao falhou! o valor informado é invalido.")            

    return saldo, extrato

def criarConta():

    agencia = (input("\nDigite Numero da sua agencia: " ))
    conta = (input("\nDigite Numero da sua Conta: " ))

    if agencia.isdigit() and conta.isdigit():
        print("======= Conta Criada com Sucesso ======= ")
        print(f"Agencia {agencia} \nNumero da conta {conta} ")
        return int(agencia), int(conta)

    else:
        print("\nerro a criar a conta")
        return None,None
    

def criacao_Usuario():
    print("====== Criacao de usuario =========")
    nome = input("Digite seu Nome: ")
    nasc = input("Digite seu Ano de Nascimento: ")
    cpf = input("Digite seu CPF: ")
    endereco_rua = input("Digite seu Rua: ")
    endereco_bairro = input("Digite seu Bairro: ")
    endereco_numero = input("Digite seu Numero da sua Casa: ")
    endereco_cidade = input("Digite sua Cidade: ")

    return {"nome":nome,"ano_nascimento":nasc,"CPF":cpf,"endereco":{endereco_rua,endereco_numero,endereco_bairro,endereco_cidade}}


def bancoDadosConta(agencia,conta):
    return {"agencia":agencia,"Conta":conta}

def listar_contas(lista1,lista2):
    print("Contas Cadastradas ") 

    if lista1 == [] or lista2 == []:
        print("Nao a contas Cadastradas")
    else:
        for listao1,listao2 in zip(lista1,lista2):
            print(f"\nNome: {listao1["nome"]} / Agencia {listao2["agencia"]}")
           
            
def Main():
    saldo = 1000
    limite_maximo = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    dado_da_Conta = []
    dados_usuarios = []
    agencia = 0
    conta = 0

    while True:

        opcao = input(menuUsuario())

        if opcao.lower() == "d".lower():

            valor = float(input("informe valor a ser depositado "))
            saldo,extrato = depositar(valor,saldo,extrato)

            print(f"Saldo Atual : {saldo} \n{extrato}")
        elif opcao.lower() == "s".lower():

            valor = float(input("informe o valor do saque:"))

            valor,saldo,extrato,numero_saques = sacar(valor,saldo,limite_maximo,limite_saques,numero_saques,extrato)
            print(valor,saldo,limite_maximo,limite_saques,numero_saques,extrato)

        elif  opcao.lower() == "e".lower():
            
            print(extratao(saldo,extrato))

        elif opcao.lower() == "nc".lower() or opcao.lower() == "nu".lower():
            
            if agencia == None or conta == None:
                print("erro na implementacao")
            elif opcao.lower() == "nc".lower():

                agencia,conta = criarConta()
                dado_da_Conta.append(bancoDadosConta(agencia,conta))
                print("\n Agora por motivos de seguranca precisamos fazer seu cadastro \n")
                dados_usuarios.append(criacao_Usuario())
                print("\nDados criados com sucesso\n")

            elif opcao.lower() == "nu".lower() :
                dados_usuarios.append(criacao_Usuario())
                print("\n Agora por motivos de seguranca precisamos fazer seu cadastro da conta \n")
                agencia,conta = criarConta()
                dado_da_Conta.append(bancoDadosConta(agencia,conta))
                print("\nDados criados com sucesso\n")
                print(dado_da_Conta)
                print(dados_usuarios)
            
                
        elif opcao.lower() == "lc".lower():
            listar_contas(dados_usuarios,dado_da_Conta)
        

        elif opcao.lower() == "q".lower():
            print("Ate mais... Volte Sempre ! ")
            break

Main()