import time

# Dados de login
login_correto = "admin"
senha_correta = "HapDame@2023"

# Lista para armazenar informações dos pacientes
pacientes = []

def realizar_login():
    """
    Realiza a autenticação do usuário no sistema.

    Solicita o login e a senha, verifica se são corretos e retorna um valor booleano.

    Returns:
        bool: True se o login for bem-sucedido, False caso contrário.
    """
    # Solicitação de login e senha
    login_digitado = input("Digite o login: ")
    senha_digitada = input("Digite a senha: ")

    # Verificação de login e senha
    if login_digitado == login_correto and senha_digitada == senha_correta:
        return True
    else:
        print("\nLogin ou senha incorretos. Tente novamente.")
        return False

def registro_paciente():
    """
    Registra as informações de um novo paciente.

    Solicita o nome e a idade do paciente, e adiciona um dicionário representando o paciente à lista de pacientes.
    """
    global pacientes
    paciente_nome = input("Digite o nome do paciente: ")
    paciente_idade = input("Digite a idade do paciente: ")

    pacientes.append({"Nome": paciente_nome, "Idade": paciente_idade})
    print(f"\nPaciente {paciente_nome} registrado com sucesso. O número total de paciente no momento é de: {len(pacientes)}.")

def medico_indisponivel():
    """
    Simula a transferência de um paciente para outro hospital após a triagem.
    """
    print("\nPaciente transferido para outro hospital após a triagem.")

def ver_lista_pacientes():
    """
    Exibe a lista completa de pacientes registrados, mostrando seus nomes e idades.
    """
    print("\nLista de Pacientes:")
    for paciente in pacientes:
        print(f"Nome: {paciente['Nome']}, Idade: {paciente['Idade']}")
    print(f"Número total de pacientes: {len(pacientes)}")

def alta_paciente():
    """
    Permite dar alta a um paciente escolhido da lista, removendo-o da lista de pacientes.
    """
    global pacientes
    if pacientes:
        print("\nLista de Pacientes:")
        for i, paciente in enumerate(pacientes):
            print(f"{i + 1}. Nome: {paciente['Nome']}, Idade: {paciente['Idade']}")

        escolha = input("Escolha o número do paciente para dar alta (1-{0}): ".format(len(pacientes)))

        try:
            indice_paciente = int(escolha) - 1

            if 0 <= indice_paciente < len(pacientes):
                paciente_alta = pacientes.pop(indice_paciente)
                print(f"\nPaciente {paciente_alta['Nome']} recebeu alta.")
            else:
                print("\nNúmero de paciente inválido. Tente novamente.")
        except ValueError:
            print("\nPor favor, insira um número válido.")
    else:
        print("\nNão há pacientes para dar alta.")

# Função principal
def main():
    """
    Função principal que controla o fluxo do programa.

    Exibe um menu de opções e chama outras funções com base nas escolhas do usuário.
    """
    # Verificação de login
    while not realizar_login():
        pass  # Continua pedindo login até que seja bem-sucedido

    while True:
        # Menu de opções
        print("\nOpções:")
        print("1. Registro de paciente")
        print("2. Médico indisponível")
        print("3. Ver lista total de pacientes")
        print("4. Alta de paciente")
        print("5. Sair")

        escolha = input("Escolha a opção (1-5): ")

        if escolha == "1":
            print("\n==============================\n")
            registro_paciente()
        elif escolha == "2":
            print("\n==============================\n")
            medico_indisponivel()
        elif escolha == "3":
            print("\n==============================\n")
            ver_lista_pacientes()
        elif escolha == "4":
            print("\n==============================\n")
            alta_paciente()
        elif escolha == "5":
            print("\n==============================\n")
            print("Saindo do programa. Até logo!")
            break
        else:
            print("\n==============================\n")
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    print("Bem-vindo ao Sistema para Controle de Registro Hospitalar!\n")
    main()
