from easygui import buttonbox
from easygui import msgbox

while True:
    msgbox("Los gehts")
    Punkte = 0
    while True:
        try:
            Punkte = Punkte + int(buttonbox(choices = ["2","4","5","75","Fertig"]))
        except:
            break
    msgbox(Punkte)
