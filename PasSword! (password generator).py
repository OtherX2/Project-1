import random
import time

randomPass = 0
character_opt = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
aPass = ""
kiy = 0
def Password_create():
    global randomPass
    randomPass = random.randint(111111111, 999999999)

def aPasser():
    global aPass
    for i in range(kiy):
        aPass += random.choice(character_opt)

print("Gracias por elegir este programa de creacion de contraseñas!")
time.sleep(1.5)
print("este programa generara una contraseñan aleatoria, ¡Recuerda anotarla para no perderla!")
modo = input("quieres una contraseña... numerica o totalmente aleatoria?... responde con n (por numerica) o a (por aleatoria)!")
if modo == "n":
    time.sleep(2)
    print("Cargando...")
    time.sleep(0.5)
    for i in range(3):
        print("...")
        time.sleep(1.5)

    Password_create()
    print("esta es tu contraseña numerica:", randomPass, "apesar de ser aleatoria no es totalmente segura al contener solo numeros")
else:
    kiy = int(input("ingresa la longitud de la contraseña"))
    print("Cargando...")
    time.sleep(0.5)
    for i in range(3):
        print("...")
        time.sleep(1.5)
    aPasser()
    print("esta es tu contraseña aleatoria", aPass, "es mas segura que la numerica! pero mas dficil de recordar")
    print("Esta contraseña puede no funcionar por los caracteres incluidos")
