import re # Importa o módulo de expressões regulares

# Inicializa o dicionário para armazenar os contatos
contatos = {}

# Define a expressão regular para o formato do telefone
# Aceita (XX) XXXX-XXXX ou (XX) XXXXX-XXXX
PADRAO_TELEFONE = r"^\(\d{2}\) \d{4,5}-\d{4}$"


while True:
    print("\nMENU:")
    print("1 - Adicionar Contato")
    print("2 - Buscar Contato")
    print("3 - Listar Todos os Contatos")
    print("4 - Remover Contato")
    print("5 - Sair")

    try:
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            nome = input("Nome do Contato: ")
            
            
            while True: 
                telefone = input(f"Telefone de {nome} (formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX): ")
                if re.fullmatch(PADRAO_TELEFONE, telefone):
                    break 
                else:
                    print("Formato de telefone inválido. Por favor, use (DD) NNNN-NNNN ou (DD) NNNNN-NNNN.")

            contatos[nome] = telefone
            print(f"Contato '{nome}' ({telefone}) adicionado/atualizado.")

        elif escolha == 2:
            nome = input("Nome do Contato a buscar: ")
            if nome in contatos:
                print(f"Telefone de {nome}: {contatos[nome]}")
            else:
                print(f"Contato '{nome}' não encontrado.")

        elif escolha == 3:
            if not contatos:
                print("Nenhum contato na lista.")
            else:
                print("--- SEUS CONTATOS ---")
                for nome_contato, tel_contato in contatos.items():
                    print(f"{nome_contato}: {tel_contato}")
                print("----------------------")

        elif escolha == 4:
            nome = input("Nome do Contato a remover: ")
            if nome in contatos:
                # Opcional: Adicionar uma confirmação antes de remover
                confirmacao = input(f"Tem certeza que deseja remover '{nome}'? (s/n): ").lower()
                if confirmacao == 's':
                    del contatos[nome]
                    print(f"Contato '{nome}' removido.")
                else:
                    print(f"Remoção de '{nome}' cancelada.")
            else:
                print(f"Contato '{nome}' não encontrado.")

        elif escolha == 5:
            print("Saindo do gerenciador de contatos. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um NÚMERO para a opção do menu.")
        continue # Pula para a próxima iteração do loop, exibindo o menu novamente.