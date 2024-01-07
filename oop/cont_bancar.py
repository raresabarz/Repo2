class ContBancar:
    #constructor
    def __init__(self, titularCont, iBan):
        # atribute, fields
        self.titularCont = titularCont
        self.iBan = iBan
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    def interogareSold(self):
        print(f'Titular {self.titularCont})
        print(f'IBAN {self.iBan})
        print(f'Sold {self.sold})
        print(f'Activ {self.activ})
        print(f'Nr de incercari {self.incercari_activare})
        print('---------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('PIN Gresit')
            self.incercari_activare += 1
    def alimentare(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold})

    def plataCard(self, suma):
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati platit suma de {suma} lei')
        else:
            print('Fonduri Insuficiente')

    def salut(self):
        print(f'Buna {self.titularCont}')
# tema
# clasa Angajat
#nume, prenume, salariu , vechime, functie
#constructor : nume, prenume ,salariu ,functie, vechime
# metode
# descriere
# marire salariu in f de vechime
# actualizare vechime (parametru noua vechime)
                   # self.vechime = noua vechime
# daca are vechime sub 5 ani(300)   peste 5 ani, (500)

