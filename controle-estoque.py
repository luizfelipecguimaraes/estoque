max_estoque = int(150)

while True:
    for c in range(1,4):
        login = str(input('Usuário: '))
        senha = str(input('Senha: '))
        if login == 'admin' and senha == '@dmiN':
            print('-='*10)
            print('Login realizado com sucesso!')
            print('-='*10)
            break
        else:
            print('Usuário ou senha inválido')
            print(f'Você tentou {c} vez(es). Limite: 3')
            if c == 3:
                print('-='*10)
                print('Você tentou o máximo de vezes!')
                print('Fechando programa por segurança')
                print('-='*10)
                exit()
    break              
    
def cadastrar(lista):
    categoria = input('Digite a categoria do produto: ')
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    produto = {'categoria': categoria, 'nome': nome, 'quantidade': quantidade}
    lista.append(produto)
    print('Cadastro realizado com sucesso!')

def consulta(lista):
    nome = input("Digite o nome do produto a ser consultado: ")
    for produto in lista:
        if produto["nome"] == nome:
            print()
            print("Informações do produto:")
            print(f"Categoria: {produto['categoria']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print()
            return
    print("Produto não foi encontrado.")

def atualização(lista):
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in lista:
        if produto["nome"] == nome:
            opcao = input("Deseja atualizar a categoria, nome ou quantidade? (C/N/Q): ").strip().upper()[0]
            if opcao == "N":
                novo_nome = input("Digite o novo nome do produto: ")
                produto["nome"] = novo_nome
            if opcao == "Q":
                nova_quantidade = int(input("Digite o novo estoque do produto: "))
                produto["quantidade"] = nova_quantidade
            if opcao == "C":
                nova_categoria = input('Digite a nova categoria do produto: ')
                produto["categoria"] = nova_categoria
            print("Produto atualizado!")
            print()
            return
    print("Produto não foi encontrado.")

def exclusão_do_produto(lista):
    nome = input("Digite o nome do produto a ser excluído: ")
    for produto in lista:
        if produto["nome"] == nome:
            lista.remove(produto)
            print("Produto excluído!")
            return
    print("Produto não foi encontrado.")

def relatorio(lista):
    print("Relatório de Produtos:")
    for produto in lista:
        print()
        print(f"Categoria: {produto['categoria']}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("------------------")
        
def quant_estoque(lista):
    print("Relatório de Produtos:")
    for categoria in lista:
        print()
        print(f"Categoria {categoria['categoria']}:", categoria["quantidade"], "unidades" )
        print("------------------")
        porcen = categoria["quantidade"]*100/max_estoque
        print('{:.2f}%'.format(porcen))

def necessidade_estoque(lista):
    print("Necessidades do sistema: ")
    print('-='*20)
    for produto in lista:
        print()
        print(f"Nome: {produto['nome']} do tipo {produto['categoria']}")
        print(f"Quantidade: {produto['quantidade']}")
        if produto['quantidade'] <= 10 :
            print('-'*10)
            print('Necessidade de realizar um novo pedido!')
            print('-'*10)
        else:
            print('-'*10)
            print('Não há necessidade de realizar um novo pedido!')
            print('-'*10)
            
def menu_do_estoque():
    print()
    print("======= MENU - CONTROLE DE ESTOQUE ======")
    print("1 - Cadastrar Produto")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Excluir Produto")
    print("5 - Exibir Relatório de Produtos")
    print("6 - Exibir Quantidade de Produtos Por Categoria")
    print("7 - Necessidades do estoque")
    print("8 - Encerrar")
    print()

produtos = []

while True:
    menu_do_estoque()
    opcao = input("Opção desejada: ")
    if opcao == "1":
        print()
        cadastrar(produtos)
    elif opcao == "2":
        print()
        consulta(produtos)
    elif opcao == "3":
        print()
        atualização(produtos)
    elif opcao == "4":
        print()
        exclusão_do_produto(produtos)
    elif opcao == "5":
        print()
        relatorio(produtos)
    elif opcao == "6":
        print()
        quant_estoque(produtos)
    elif opcao == "7":
        print()
        necessidade_estoque(produtos)
    elif opcao == "8":
        print("Terminando o programa...")
        print('-='*10)
        break
    else:
        print("Inválido. Digite novamente.")
