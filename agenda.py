# Inicializa o dicionário para armazenar os contatos
contatos = {}

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
      telefone = input(f"Telefone de {nome}: ")
      contatos[nome] = telefone
      print(f"Contato {nome}: {telefone} adicionado/atualizado.")
    elif escolha == 2:
      nome = input("Nome do Contato: ")
      if nome in contatos:
        print(f"Telefone de {nome}: {contatos[nome]}")
      else:
        print("Contato não encontrado.")
    elif escolha == 3:
      if not contatos:
        print("Nenhum contato na lista.")
      else:
        print("--- SEUS CONTATOS ---")
        for nome_contato, tel_contato in contatos.items():
          print(f"{nome_contato}: {tel_contato}")
        # A linha abaixo estava indented incorretamente
        print("----------------------")
    elif escolha == 4:
      nome = input("Nome do Contato Deseja Excluir: ")
      # As linhas abaixo tinham um nível de indentação extra
      if nome in contatos:
        del contatos[nome]
        print(f"Contato '{nome}' removido.")
      else:
        print("Nome não Encontrado.")
    elif escolha == 5:
      print("Saindo do gerenciador de contatos. Até mais!")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
  except ValueError:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")