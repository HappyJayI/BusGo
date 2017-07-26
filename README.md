# BusGo the "HappyBox" prototype
### Raspberry pi3 based RFID tagging & video player for public bus users 

## Summary
* If handicapped person tag rfid card in busstop, it informs to bus driver to do careful drive and pick up
* If handicapped person get in bus and tag rfid card, HappyBox display campaign video for leaving 
seats empty for handicapped person.
* If bus are going to stop, HappyBow shows next busstop & simple information near busstop

## BOM
* Raspberry pi3 : 2 ea
* RFID reader : 1 ea
* RFID card : 2 ea
* Bread board : 2 ea
* Display 5 inch : 1 ea
* Video : 5 ea ( inform, campaign 3, busstop )

### BusGoServer( for seat )
* Raspberry pi3
* Display

### BusGoClient( for busstop or bus entrance )
* Raspberry pi3
* RFID reader

## Architecture
![Waiting](/image/BusGoArchitecture.jpg)

## Use Cases
![Waiting](/image/BusGo1.jpg)
![Get In](/image/BusGo2.jpg)
![Busstop](/image/BusGo3.jpg)

## Installation
* sodu pip install python-dev
* git clone https://github.com/lthiery/SPI-Py.git
* cd SPI-Py
* sudo python setup.py install
* git clone https://github.com/mxgxw/MFRC522-python.git
* sudo pip install Web.py
* sudo pip install subprocess
* BusGo Client : run MFRC522.py as service
* BusGo Server : run BusGoWeb.py as service

## References
*RFID setting :  
http://www.instructables.com/id/Raspberry-Pi-3-Model-B-MIFARE-RC522-RFID-Tag-Readi/  
*run RFID tagging as Service :  http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/ 