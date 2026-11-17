# Laskin v1.0

def yhteenlasku(a, b):
    return a + b

def vahennyslasku(a, b):
    return a - b

def kertolasku(a, b):
    return a * b

def jakolasku(a, b):
    if b == 0:
        return "Nollalla jakaminen ei ole sallittua."
    return a / b

print ("Laskin v1.0")
print ("5 + 3 =", yhteenlasku(5, 3))
print ("10 - 4 =", vahennyslasku(10, 4))
print ("6 * 7 =", kertolasku(6, 7))
print ("8 / 2 =", jakolasku(8, 2))
