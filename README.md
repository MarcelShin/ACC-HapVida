# Sistema para Controle de Registro Hospitalar

Bem-vindo ao Sistema para Controle de Registro Hospitalar! Este é um programa simples em Python para gerenciar o registro de pacientes em um hospital. Abaixo, você encontrará informações sobre como utilizar e entender o código.

## Requisitos
Certifique-se de ter o Python instalado em seu ambiente antes de executar este programa

## Funcionalidades
1. Realizar Login
Antes de acessar as funcionalidades do programa, é necessário realizar o login. O login padrão é definido como:
- Login: admin
- Senha: HapDame@2023

2. Registro de Paciente
Permite registrar informações de um paciente, incluindo nome e idade.

3. Médico indisponível
Simula a transferência de um paciente para outro hospital após a triagem, devido a falta do médico da especialidade desejada.

4. Ver Lista Total de Pacientes
Exibe a lista completa de pacientes registrados, incluindo nome e idade.

5. Alta de Paciente
Permite dar alta a um paciente escolhido da lista.

6. Sair
Encerra o programa.

## Funcionamento
1. O programa inicia solicitando o login e a senha do usuário.

2. Após o login bem-sucedido, o usuário tem acesso a um menu de opções.

3. Opções disponíveis:
   - **Registro de Paciente:** Registra um novo paciente, coletando nome e idade.
   - **Médico indisponível:** Simula a transferência de um paciente para outro hospital após triagem, logo, que o mesmo não ocupou o hospital, independente do motivo.
   - **Ver Lista Total de Pacientes:** Exibe a lista de todos os pacientes registrados, juntamente com sua numeração.
   - **Alta de Paciente:** Dá alta ao paciente na lista de acordo com a numeração escolhida, se houver.
   - **Sair:** Encerra o programa.

## Variáveis
1. login_correto:
- Tipo: String
- Função: Armazena o valor do login correto para autenticação no sistema.

2. senha_correta:
- Tipo: String
- Função: Armazena o valor da senha correta para autenticação no sistema.

3. pacientes:
- Tipo: Lista
- Função: Armazena dicionários contendo informações dos pacientes, como nome e idade.

4. realizar_login():
- Função: Solicita o login e a senha do usuário, verifica se são corretos e retorna um valor booleano indicando se o login foi bem-sucedido.

5. registro_paciente():
- Função: Solicita informações de um novo paciente (nome e idade) e adiciona um dicionário representando o paciente à lista de pacientes.

6. medico_indisponivel():
- Função: Simula a transferência de um paciente para outro hospital após a triagem.

7. ver_lista_pacientes():
- Função: Exibe a lista completa de pacientes registrados, mostrando seus nomes e idades.

8. alta_paciente():
- Função: Permite dar alta a um paciente escolhido da lista, removendo-o da lista de pacientes.

9. main():
- Função: Função principal que controla o fluxo do programa. Chama outras funções com base nas escolhas do usuário no menu.

10. name == "main":
- Condição: Verifica se o script está sendo executado como o programa principal.
- Função: Inicializa o programa chamando a função principal (main()) quando o script é executado diretamente.

## Integrantes
Marcelo Vieira de Melo - RM: 552953
Caio Hideki Cardenas Ishizu – RM: 553630

## Observações
- O código é um exemplo básico e pode ser estendido para atender a requisitos específicos do sistema hospitalar.
- Certifique-se de substituir os dados de login padrão por informações seguras em um ambiente de produção.

---

**Observação:** Antes de implementar ou utilizar este código, verifique se está em conformidade com as regulamentações locais e garanta que o sistema atenda aos padrões de segurança necessários.
