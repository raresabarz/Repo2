# functie = logica delimitata care poate fi refolosita

def printGreeting():
    print("Buna ziua! Bine ati venit!")

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a, b, c):
    return(a + b + c) / 3

def piValue():
    return 3.14
# exercitiu
# daca pers e majora, altfel false

def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

def celmaimareNumar(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c



# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('A', 'Rares')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(17))
print(verificareMajor(18))
# se ia varsta utilizatorului
age = int(input('introduceti varsta dvs --> '))
if verificareMajor(age):
    print('Cont creat')
else:
    print('Nu ai varsta necesara')

print(celmaimareNumar(10, 1, 6))

# oop
# variabile --> atribute, proprietati sau fields
# functii --> metode
