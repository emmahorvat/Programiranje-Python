import random

x = random.randint(1, 10)

y = int(input("Pogodi broj x"))

if x == y:
    print("Bravo, pogodio si traženi broj!")
else:
    print("Netočno, traženi broj je bio {0}" .format(x))
    