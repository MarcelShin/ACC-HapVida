from machine import Pin, PWM
import time

# Configuração dos pinos
pir_outside_pin = Pin(14, Pin.IN)  # Pino do sensor de presença do lado de fora
pir_inside_pin = Pin(12, Pin.IN)   # Pino do sensor de presença do lado de dentro
servo_pin = Pin(13)                # Pino do motor servo

# Configuração do PWM para o servo
servo_pwm = PWM(servo_pin, freq=50)

# Variável para contar o número de pacientes
pacient_counter = 0

# Função para abrir a porta
def abrir_porta():
    for duty_cycle in range(40, 115, 1):
        servo_pwm.duty(duty_cycle)
        time.sleep_ms(15)
    time.sleep(2)  # Aguarda 2 segundos com a porta aberta
    fechar_porta()

# Função para fechar a porta
def fechar_porta():
    for duty_cycle in range(115, 40, -1):
        servo_pwm.duty(duty_cycle)
        time.sleep_ms(15)

# Loop principal
while True:
    if pir_outside_pin.value() == 1:  # Sensor de fora acionado
        pacient_counter += 1
        print("Paciente entrou. Total de pacientes:", pacient_counter)
        abrir_porta()
        time.sleep(5)  # Aguarda 5 segundos antes de permitir nova detecção
    elif pir_inside_pin.value() == 1:  # Sensor de dentro acionado
        pacient_counter -= 1
        print("Paciente saiu. Total de pacientes:", pacient_counter)
        fechar_porta()
        time.sleep(5)  # Aguarda 5 segundos antes de permitir nova detecção
# Esqueleto do projeto
