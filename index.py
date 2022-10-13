from datetime import datetime

now = datetime.now().strftime("%H:%M:%S")

def sayHello() :
    if now < '18:00:00.0':
        print("Bonjour")
    else:
        print("Bonsoir")


current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

