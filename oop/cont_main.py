import oop
from oop.cont_bancar import ContBancar

cont1 = oop.cont_bancar.ContBancar('Abarzaei Rares', 'ROBTRL00123')
cont2 = oop.cont_bancar.ContBancar('Abarzaei Vlad', 'ROBTRL00122')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentare(300)
cont2.alimentare(2000)
cont1.alimentare(1200)

cont1.interogareSold()
cont2.interogareSold()
