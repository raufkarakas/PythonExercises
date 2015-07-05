__author__ = 'rkarakas'

import random

def nameGenerator():
    nameList = ["Ali", "Veli", "Ahmet", "Mehmet", "Ragip", "Rauf", "Omer", "Faruk", "Lokman", "Soner", "Mahmut"]
    surnameList = ["Ozturk", "Delice", "Kaya", "Tas", "Cimen", "Gok", "Dagli", "Ordulu", "Guzelce", "Kayabasi"]

    return "%s %s" %(random.choice(nameList), random.choice(surnameList))

for i in range(5):
    print(nameGenerator())