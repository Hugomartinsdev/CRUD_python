carrinho = []
def adicionar_na_caixa():
    nome = input('Escolha o que colocar no carrinho: ')
    quantidade= int(input('Escolha a quantidade para colocar no carrinho: '))
    preco = float(input("Qual o valor: "))
    produto = {}
    produto.update({'Nome': nome, "Quantidade": quantidade, 'Preço': preco})
    return produto


def remover_do_carrinho():
    nome = input('Qual o nome do produto você quer tirar?: ')
    quantidade = int(input('Qual a quantidade que você quer retirar do produto?: '))
    for item in carrinho:
        if item['Nome'] == nome:
            if item["Quantidade"] < quantidade:
                print('Esta retirando mais do você já tem')
                print(f'Você possui no carrinho {item['Quantidade']} e você pediu para retirar {quantidade}')
            else:
                    item['Quantidade'] = item['Quantidade'] - quantidade
                    if item['Quantidade'] == 0:
                            carrinho.remove(item)
                            print('\nRemoção feita com sucesso\n')
                            vizualizar_o_carrinho()
                    else:
                        print('\nRemoção feita com sucesso\n')
                        vizualizar_o_carrinho()
        else:
            print(f'{nome} não foi encontrado no carinho')

def valor_total():
    soma=0
    for valor in carrinho:
        soma += valor['Preço']*valor['Quantidade']
    return print(f'Valor total no carrinho: R$ {soma}')


def vizualizar_o_carrinho():
    print('----Carrinho----')
    if len(carrinho) == 0:
        print('Carrinho Vazio')
    else:
        for carro in carrinho:
            print(f'Nome do produto: {carro['Nome']}\nQuantidade: {carro["Quantidade"]}\nValor:R$ {carro['Preço']}')
        valor_total()
    print('----------------')

def comprar():
    vizualizar_o_carrinho()
    print("finalizar conta?")
    respostaa = input('S OU N: \n')
    if respostaa == 'S':
        print('Compra finalizada')
        carrinho.clear()
    else:
        print('Compra cancelada')

def menu():
    print('----MENU----')
    print('1-ADICIONAR NO CARRINHO')
    print('2-REMOVER DO CARRINHO')
    print('3-VIZUALIZAR O CARRINHO')
    print('4-COMPRAR')
    print('5-SAIR')
    print('------------')

if __name__ == '__main__':
    menu()
    resposta = int(input())
    while True:
        match resposta:
            case 1:
                carrinho.append(adicionar_na_caixa())
                print('\nItem adicionado no carrinho\n')
                menu()
                resposta = int(input())
            case 2:
                remover_do_carrinho()
                menu()
                resposta = int(input())
            case 3:
                vizualizar_o_carrinho()
                menu()
                resposta = int(input())
            case 4:
                comprar()
                menu()
                resposta = int(input())
            case 5:
                print('Saindo...')
                break
            case default:
                print('Escolha uma opção valida\n\n')
                menu()
                resposta = int(input())