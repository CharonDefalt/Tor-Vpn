#Made_By_defalt
#This script change your ip
#pip install signal
#pip install stem

#If you want you can make crontab for it to run it after some time
#For Example : */15 * * * * /usr/bin/python3 YourPath/ip-changer.py
#Up command run's script in every 15 minutes


# Importment : You must delete # behind ControlPort and HashPassword in torrc file 


from stem import Signal
from stem.control import Controller

def change_tor_ip():
    with Controller.from_port(port=9085) as controller:   # i changed my tor contorl port in torrc file , the default is 9051
        controller.authenticate("16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C") # in " " you must set your own Hash password , you can find it in torrc
        controller.signal(Signal.NEWNYM)
        print("New IP address requested.")

if __name__ == "__main__":
    change_tor_ip()
