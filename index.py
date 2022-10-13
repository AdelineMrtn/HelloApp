from datetime import datetime

now = datetime.now().strftime("%H:%M:%S")
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
today18am = now.replace(hour=18, minute=0, second=0, microsecond=0)

def sayHello() :
    if today8am < now < today18am:
        print("Bonjour")
    else:
        print("Bonsoir")

sayHello()

