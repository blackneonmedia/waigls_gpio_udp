import RPi.GPIO as GPIO
import socket
import time

# Konfiguration
BUTTON_GPIO_PIN = 18  # Auf den Pin ändern an dem der Taster angeklemmt ist
UDP_IP = "192.168.1.100"  # Ziel-IP-Adresse
UDP_PORT = 5005           # Ziel-Port
MESSAGE = b"Servus ich bin eim Tastendruck!"  # Nachricht, die gesendet werden soll

# GPIO einrichten
GPIO.setmode(GPIO.BCM)  # BCM-Nummerierung verwenden
GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-Up aktivieren

# UDP-Socket einrichten
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print("Warten auf Tasterdruck...")
    while True:
        button_state = GPIO.input(BUTTON_GPIO_PIN)
        if button_state == GPIO.LOW:  # Taster gedrückt (bei Pull-Up)
            print("Taster gedrückt! Sende UDP-Nachricht...")
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            time.sleep(0.5)  # Entprellen
except KeyboardInterrupt:
    print("Beenden...")
finally:
    GPIO.cleanup()  # GPIO freigeben
