def depositar(valor,saldo,extrato,/):
    saldo+=valor
    extrato+=f"Deposito: R${valor:.2f}\n"
    return saldo,extrato
def sacar(*,saque,saldo,extrato):    
    saldo-=saque
    extrato+=f"Saque: R${saque:.2f}\n"
    return saldo,extrato
def extrato_conta(extrato,/,*,saldo):
    print('\n#################### Extrato ####################')        
    print('Não foi realizado movimentações' if not extrato else extrato)
    print(f'Seu saldo é de: R${saldo:.2f}')
    print('#################################################')
def localizar_cpf(cpf,usuarios):    
    usuarios_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtro[0] if usuarios_filtro else None
def new_user(usuario):
     cpf = input("Informe o CPF (somente números): ")
     user=localizar_cpf(cpf,usuario)
     if user:
         print("\nJá existe um usuário com esse cpf")
         return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
     return {"nome": nome,"cpf": cpf,"data": data_nascimento,"endereco": endereco}
def new_acc(agencia,numero,usuario):
     cpf = input("Informe o CPF (somente números): ")
     user=localizar_cpf(cpf,usuario)
     if user:
        return {"agencia":agencia,"numero":numero,"usuario":usuario}
        
     print("Usuário não encontrado no banco!")
def listar(contas):
    if contas:
        for cc in contas:
            print(f'\nAgência: {cc["agencia"]}\nConta: {cc["numero"]}\nTitular: {cc["usuario"]}\n')
            print("=" * 50)
    else:
        print('Não existem contas cadastradas')
def main():
    menu= """
        Banco NE
        
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Criar usuário
        5 - Criar conta
        6 - Listar contas
        7 - Sair
    => """
    AGENCIA = "0001"
    saldo=0
    extrato=""
    limitesaque=500
    limite_saque_dia=3
    quantidade_saque=0
    usuarios = []
    contas = []

    while True:
        opcao=int(input(menu))
        
        if opcao==1:
            valor=float(input('Informe o valor a ser depositado: '))       
            if(valor<=0):
                print('Valor invalido!')
            else:
                saldo,extrato=depositar(valor,saldo,extrato)            
        elif opcao==2:
            if(quantidade_saque==limite_saque_dia):
                print('Limite de saque diario atingido. Tente novamente outro dia')
            else:
                saque=float(input('Digite o valor que deseja sacar: '))
                if(saque<=0):
                    print('Valor invalido! Não é possivel fazer saque negativo.')
                elif(saque>limitesaque):
                    print('Valor invalido! O valor de saque é maior que o limite.')
                elif(saque>saldo):
                    print('Não existe saldo suficiente para esse saque.')
                else:
                    saldo,extrato=sacar(saque=saque,saldo=saldo,extrato=extrato)   
                    quantidade_saque+=1             
        elif opcao==3:
            extrato_conta(extrato,saldo=saldo)        
        elif opcao==4:
            user=new_user(usuarios)
            usuarios.append(user)
            print("\nUsuário criado!")
        elif opcao==5:
            num_conta=len(contas)+1
            
            conta=new_acc(AGENCIA,num_conta,usuarios)
            
            if conta:
                contas.append(conta)
                print("\nConta criada!")
        elif opcao==6:
            listar(contas)
        elif opcao==7:
            print("Volte Sempre!")
            break
        else:
            print('Valor invalido. Tente novamente!')
main()
