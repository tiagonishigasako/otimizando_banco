from time import sleep



menu = f"""{'Digite a opçao desejada':^40}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


inicio = f"""
{"-=" * 20}
{"Bem vindo ao bit bank.":^40}

[E] Entrar numa conta existente.
[N] Criar uma nova conta.

=>"""


contas = {}
usuarios = {}
LIMITE_SAQUES = 3

def saque (*,saldo , valor , limite, numero_saques):
    if valor > 0:
        if saldo >= valor:
            if valor <= limite:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= valor
                    numero_saques += 1
                    extrato = f'Saque: R$ {valor:.2f}\n'
                    retorno_statos = "Sacado"
                else:
                    retorno_statos = "Operação falhou! Número máximo de saques excedido."
                    extrato = 0
            else:
                retorno_statos = f"O valor maximo para saques é de R${limite:.2f}"
                extrato = 0
        else: 
            retorno_statos = "Saldo insuficiente para saque."
            extrato = 0
    else:
        retorno_statos = "O valor nao pode ser negativo"
        extrato = 0

    return saldo, extrato, numero_saques, retorno_statos


def deposito(saldo, valor):
    saldo += valor
    extrato = f"Depósito: R$ {valor:.2f}\n" 
    return saldo, extrato

def calula_extrato(saldo,/,*,extrato):
    global conta_atual
    conta_atual['saldo'] = saldo
    conta_atual['extrato'] += extrato
    return extrato


def criar_usuario(cpf):
    lista = {}
    lista['nome'] =  input('nome')
    lista['nascimento'] = input('data_nascimento')
    lista['endereco'] = input('Endereco logradouro, numero, bairro, cidade/sigla estado')
    lista['conta'] = []
    usuarios[cpf] = lista

    print(cpf)
    print('novo usuario criado')

    criar_conta(cpf)
    
    return

def criar_conta(cpf):
    conta = {}
    conta['agencia'] = "0001"
    conta['usuarios'] = cpf
    conta['saldo'] = 0
    conta['extrato'] = ''
    conta['limite'] = 500
    conta['numero_saques'] = 0
    usuarios[cpf]['conta'].append(len(contas))
    contas[len(contas)] = conta
    print('conta criada')
    return

while True:
    while True:

        opcao = " "
        while opcao not in "en":
            opcao = input(inicio).lower().strip()[0]
        if opcao == "e":
            cpf = int(input('Digite seu cpf: '))
            if cpf in usuarios:
                if len(usuarios[cpf]["conta"]) !=0:
                    print(f'Foi encontrado {len(usuarios[cpf]["conta"])} para esse cpf')
                    print('As contas associadas a esse cpf sao: ', end=' ')
                    for i in usuarios[cpf]['conta']:
                        print(f'Conta : {i}',end= ' ')
                    print()
                    conta = ' '
                    while conta not in usuarios[cpf]['conta']:
                        conta = int(input('Digite qual conta deseja entrar: '))
                    break
                else:    
                    conta = 0
                    break
            else:
                print(f'O Cpf {cpf} não foi encontrado.')
                sleep(1)
        if opcao == "n":
            while opcao not in "uc":
                cpf = int(input('Digite seu cpf: '))
                if cpf in usuarios:
                    print(f'O cpf {cpf} ja se encontra em nossa base de dados.')
                    nova_conta = ' '
                    while nova_conta not in "sn":
                        nova_conta = input('Deseja criar outra conta?: [S/N]').lower().strip()[0]
                    if nova_conta == "s":
                        criar_conta(cpf)
                        break
                    else:
                        break
                else:
                    print('Cliente nao encontrado: ')
                    novo_cliente = ' '
                    while novo_cliente not in 'sn':
                        novo_cliente = input('Deseja cadastrar novo usuario: [S/N] ').lower().strip()[0]
                    if novo_cliente == 's':
                        criar_usuario(cpf)
                        break
                    else:
                        break
                        
    

    conta_atual =  contas[usuarios[cpf]['conta'][conta]]
    usuario_atual = usuarios[cpf]
    print(usuario_atual)

                        
    print(f'Bem vindo {usuario_atual['nome']}\nSeu saldo é de {conta_atual['saldo']}')




    while True:
        valor = 0.00


        print('-='*20)
        print(f'{f'***Saldo = R${conta_atual['saldo']:.2f}***':^40}')
        opcao = input(menu)
        

        if opcao == "d":
            valor  = float(input('Informe o valor do depósito: R$'))
            
            saldo, extrato_retorno = deposito(conta_atual['saldo'],valor)
            calula_extrato(saldo, extrato = extrato_retorno)

        if opcao == "s":
            valor = float(input('Informe o valor do saque: R$'))
            saldo , extrato, numero_saques , retorno_statos = saque(saldo=conta_atual['saldo'], valor=valor , limite=conta_atual['limite'], numero_saques=conta_atual['numero_saques'])
            if retorno_statos == 'Sacado':
                print('aqui')
                calula_extrato(saldo, extrato= extrato)
                print('ali')
                print(retorno_statos)
            else:
                print(retorno_statos)
            conta_atual['numero_saques'] = numero_saques

            
            

        if opcao == "e":
            print('-='*20)
            print(f'{'**Extrato**':^40}')
            print(f'\nO saldo da sua conta é R${conta_atual['saldo']:.2f}')
            print(conta_atual['extrato'])
        
        if opcao == 'q':
            break
    print(f'{'Até a proxima.':^40}')


    


