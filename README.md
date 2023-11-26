# Controle de Acesso a hospitais públicos.

## Descrição
Este código implementa um sistema simples de controle de acesso para hospitais. Ele utiliza um motor servo para controlar a abertura e o fechamento de uma porta com base na detecção de presença por sensores de movimento.

## Hardware Utilizado
- Arduino Uno R3
- Sensor de presença externo (PIR) no pino 14
- Sensor de presença interno (PIR) no pino 12
- Motor servo no pino 13

## Funcionamento
1. O programa fica em um loop infinito, verificando continuamente a detecção de presença nos sensores externo e interno.
2. Se o sensor externo detecta movimento, o programa incrementa o contador de pacientes, exibe uma mensagem e abre a porta.
3. Se o sensor interno detecta movimento, o programa decrementa o contador de pacientes, exibe uma mensagem e fecha a porta.
4. Após cada detecção, o programa aguarda 5 segundos antes de permitir uma nova detecção.

## Configuração do PWM
- O PWM é configurado para o motor servo no pino 13 com uma frequência de 50 Hz.

## Variáveis
- `pir_outside_pin`: Pino do sensor de presença externo.
- `pir_inside_pin`: Pino do sensor de presença interno.
- `servo_pin`: Pino do motor servo.
- `servo_pwm`: Objeto PWM para controlar o motor servo.
- `pacient_counter`: Contador de pacientes.

## Funções
1. `abrir_porta()`: Abre gradualmente a porta controlada pelo motor servo.
2. `fechar_porta()`: Fecha gradualmente a porta controlada pelo motor servo.

## Observações
- Certifique-se de conectar corretamente os componentes aos pinos especificados.
- Este código é um exemplo básico e pode ser estendido para atender a requisitos específicos dos hospitais.
- Antes de implementar ou utilizar este código, verifique se está em conformidade com as regulamentações locais e garanta que o sistema atenda aos padrões de segurança necessários.

## Integrantes
- Marcelo Vieira de Melo - RM: 552953
- Caio Hideki Cardenas - RM: 553630
