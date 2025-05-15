class armamento:
    daño = 100
    acc_slots = 5
melee = armamento()
print(melee.daño)
melee.daño = 150
print(melee.daño)

print(melee.acc_slots)
melee.acc_slots = 7
print(melee.acc_slots)