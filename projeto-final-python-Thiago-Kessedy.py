# SISTEMA DE CADASTRO DE LOJA

# Lista onde os produtos serão armazenados como dicionários
produtos = []
# Variável usada para gerar IDs automáticos
ultimo_id = 0

#  Cadastrar produto

def cadastrar_produto():
    global ultimo_id  # Permite alterar a variável global ultimo_id

    print("Cadastro de Produto")
    nome = input("Nome do produto: ").strip()  # Recebe o nome do produto
    if not nome:  # Verifica se o nome está vazio
        print("Erro: nome não pode ser vazio.")
        return

    try:
        preco = float(input("Preço: R$ "))  # Recebe o preço
        estoque = int(input("Quantidade em estoque: "))  # Recebe quantidade
    except ValueError:
        print("Erro: valores inválidos.")  # Erro se não for número
        return

    # Verifica se são valores positivos
    if preco < 0 or estoque < 0:
        print("Erro: preço e estoque devem ser valores positivos.")
        return

    # Gera um novo ID automaticamente
    ultimo_id += 1
    produto = {
        "id": ultimo_id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    # Adiciona o novo produto à lista
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

#  Listar produtos

def listar_produtos():
    print("Lista de Produtos")
    if not produtos:  # Verifica se a lista está vazia
        print("Nenhum produto cadastrado.")
        return

    # Percorre os produtos e exibe um por um
    for p in produtos:
        print(f"ID: {p['id']} | Nome: {p['nome']} | "
              f"Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")

# UPDATE – Atualizar produto

def atualizar_produto():
    print("Atualizar Produto")
    try:
        id_busca = int(input("Digite o ID do produto: "))  # ID do produto a buscar
    except ValueError:
        print("ID inválido.")
        return

    # Percorre a lista para encontrar o produto
    for p in produtos:
        if p["id"] == id_busca:
            print(f"Produto encontrado: {p['nome']}")

            # Atualiza nome (opcional)
            novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
            if novo_nome:
                p["nome"] = novo_nome

            try:
                # Atualiza preço (opcional)
                novo_preco = input("Novo preço (deixe vazio para manter): ")
                if novo_preco:
                    p["preco"] = float(novo_preco)

                # Atualiza estoque (opcional)
                novo_estoque = input("Novo estoque (deixe vazio para manter): ")
                if novo_estoque:
                    p["estoque"] = int(novo_estoque)
            except ValueError:
                print("Valores inválidos.")  # Caso o usuário digite texto
                return

            print("Produto atualizado com sucesso!")
            return

    print("Produto não encontrado.")  # Caso não encontre o ID

# DELETE – Remover produto

def remover_produto():
    print("Remover Produto")
    try:
        id_busca = int(input("ID do produto a remover: "))  # ID a remover
    except ValueError:
        print("ID inválido.")
        return

    # Procura o produto na lista
    for p in produtos:
        if p["id"] == id_busca:
            produtos.remove(p)  # Remove o produto
            print(f"Produto '{p['nome']}' removido com sucesso!")
            return

    print("Produto não encontrado.")  # Caso não exista

# RELATÓRIO – Análise simples

def gerar_relatorio():
    print("Relatório da Loja")
    if not produtos:  # Verifica se há produtos cadastrados
        print("Nenhum dado disponível.")
        return

    # Soma total de unidades no estoque
    total_itens = sum(p["estoque"] for p in produtos)
    # Soma o valor monetário total do estoque
    valor_total_estoque = sum(p["preco"] * p["estoque"] for p in produtos)
    # Encontra o produto mais caro
    produto_mais_caro = max(produtos, key=lambda x: x["preco"])

    # Exibe os resultados
    print(f"Quantidade total de itens em estoque: {total_itens}")
    print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
    print(f"Produto mais caro: {produto_mais_caro['nome']} - "
          f"R$ {produto_mais_caro['preco']:.2f}")

# MENU PRINCIPAL
def menu():
    while True:  # Loop principal do sistema
        print("SISTEMA DE LOJA")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("5 - Gerar relatório")
        print("6 - Sair")
     

        opcao = input("Escolha uma opção: ")  # Escolhe uma ação

        # Chama as funções conforme a escolha
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("Encerrando o sistema... Até a próxima!")
            break  # Encerra o programa
        else:
            print("Opção inválida, tente novamente.")  # Se digitar algo fora das opções

# Iniciar o programa
menu()  # Chama o menu principal para rodar o sistema

