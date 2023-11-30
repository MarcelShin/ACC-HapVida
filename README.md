# Sistema para Controle de Registro Hospitalar

## Descrição
Este código implementa um sistema simples para o controle de registro hospitalar. Os usuários são autenticados por meio de um login e senha, e o sistema permite registrar, transferir, dar alta e visualizar a lista de pacientes.

## Dados de Login
- Login Padrão: "admin"
- Senha Padrão: "HapDame@2023"

## Funcionamento
1. O programa inicia solicitando o login e a senha do usuário.
2. Após o login bem-sucedido, o usuário tem acesso a um menu de opções.
3. Opções disponíveis:
   - **Registro de Paciente:** Registra um novo paciente, coletando nome e idade.
   - **Paciente Transferido:** Simula a transferência de um paciente para outro hospital após triagem, visando que o mesmo não ocupou o hospital, independente do motivo.
   - **Ver Lista Total de Pacientes:** Exibe a lista de todos os pacientes registrados.
   - **Alta de Paciente:** Dá alta ao primeiro paciente na lista, se houver.
   - **Sair:** Encerra o programa.

## Variáveis
- `login_correto`: Login padrão para acesso ao sistema.
- `senha_correta`: Senha padrão para acesso ao sistema.
- `pacientes`: Lista para armazenar informações dos pacientes.

## Funções
1. `realizar_login()`: Realiza o processo de autenticação do usuário.
2. `registro_paciente()`: Registra um novo paciente e exibe o número total de pacientes.
3. `paciente_transferido()`: Simula a transferência de um paciente para outro hospital.
4. `ver_lista_pacientes()`: Exibe a lista de todos os pacientes registrados.
5. `alta_paciente()`: Dá alta ao primeiro paciente na lista, se houver.

## Observações
- O código é um exemplo básico e pode ser estendido para atender a requisitos específicos do sistema hospitalar.
- Certifique-se de substituir os dados de login padrão por informações seguras em um ambiente de produção.

---

**Observação:** Antes de implementar ou utilizar este código, verifique se está em conformidade com as regulamentações locais e garanta que o sistema atenda aos padrões de segurança necessários.
