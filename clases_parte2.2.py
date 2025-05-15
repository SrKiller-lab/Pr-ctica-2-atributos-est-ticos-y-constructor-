#Gomez Lopez Sergio
class armamento:
    daño = 100 #primero se le dan el valor principal a los atributos
    acc_slots = 5
melee = armamento() #esta parte es para que muestre en la terminal el valor estatico y seguido de eso el valor modificado en esta parte del codigo, al igual que la zona de abajo
print(melee.daño)
melee.daño = 150
print(melee.daño)

print(melee.acc_slots)
melee.acc_slots = 7
print(melee.acc_slots)
