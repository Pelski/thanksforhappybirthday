from time import sleep
import pyautogui as pg

pg.PAUSE = 0.5
pg.FAILSAFE = False

text = pg.prompt(text='Wpisz tekst podziekowania (bez polskich znakow)', title='Birthday', default='')
pg.alert(text='Kliknij OK i umiesc kursor w polu od ktorego ma zaczac ', title='Birthday', button='OK')
sleep(10)

while True:
    try:
        pg.typewrite(text)
        pg.press('return')
        sleep(2)
        for x in range(14):
            pg.press('tab')
    except KeyboardInterrupt:
        print "Koniec, do zobaczenia za rok."
