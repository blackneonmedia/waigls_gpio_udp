# Pi: Tasterinput zu UDP senden

## Voraussetzungen

1. Python-Bibliotheken installieren:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   sudo apt install python3-pip
   pip3 install RPi.GPIO

2. Taster mit dem richtigen GPIO verbinden (Standard Pin 18). Im Script ist der Pull-Up aktviert. Kannste auch zu PullDown ändern.
  
3. das Script einfach unter sonstwo (Stanard zB. ./Home/udp_button.py) speichern. Einfach ins Wunschverzeichnis wechseln und mit vi oder nano erstellen:

   ```bash
   # Verzeichnis erstellen:
   sudo mkdir ./udp_app
   # ins Verzeichnis wechseln:
   sudo cd ./udp_app
   # py. schreiben:
   vi udp_button.py
   # inhalt aus Script einfügen und mit ":wq" speichern

4. Script starten:

   ```bash
    sudo python3 ./udp_app/udp_button.py
    
    
### für Broadcast einfach die Zeile mit der Ziel-IP auskommentieren oder löschen.
