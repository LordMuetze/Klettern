import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
TabellenListe = ["FinaleMannlich9","FinaleWeiblich9"]

#----------------------------------------------------------------------------------------------------

from operator import *
from time import *
from tkinter import *

#----------------------------------------------------------------------------------------------------

liste = []
x = 1
tabelle = ""
ROOT = Tk()
Textsize = int(40*(ROOT.winfo_screenheight()/1080+ROOT.winfo_screenwidth()/1920)/2)
ROOT.overrideredirect(True)
ROOT.geometry("{0}x{1}+0+0".format(ROOT.winfo_screenwidth(), ROOT.winfo_screenheight()))
ROOT.focus_set()  # <-- move focus to this widget
ROOT.bind("<Escape>", lambda e: e.widget.quit())

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class Kletterer:
    def __init__(self, Vorname, Nachname, FinalPunktzahl, T, VT, B, VB):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Name = Vorname + " " + Nachname
        self.FinalPunktzahl = FinalPunktzahl
        self.Rohergebnis = str(T) + "T" + str(VT) + " " + str(B) + "B" + str(VB)
#----------------------------------------------------------------------------------------------------


def main():
    global x
    global tabelle
    global liste
    global TabellenBlatt
    x = 1

    Altersklasse = TabellenBlatt.cell(1,10).value
    print(Altersklasse)
    
    #tabelle = "\n %-15s %-20s %-30s" % ("Platz", "Ergebnis", "Name")
    print(Altersklasse)

    AllesDatensaetze = TabellenBlatt.get_all_records()
    AnzahlZeilen = len(AllesDatensaetze)


    LABEL = Label(ROOT,text=tabelle,font="Times "+str(Textsize)+" bold",justify=LEFT)
    LABEL.pack()
    ROOT.update()
    print("\nLabel erstellt\n")



    while x <= AnzahlZeilen:

        # string = "global x; Nummer = 'nummer' + str(x)"
        # exec(string)

        x+=1
        
        Vorname = TabellenBlatt.cell(x,2).value
        Nachname = TabellenBlatt.cell(x,3).value
        FinalPunktzahl = TabellenBlatt.cell(x,4).value
        T = TabellenBlatt.cell(x,5).value
        VT = TabellenBlatt.cell(x,6).value
        B = TabellenBlatt.cell(x,7).value
        VB = TabellenBlatt.cell(x,8).value

        print(Vorname,Nachname)

        Nummer = Kletterer(Vorname, Nachname, FinalPunktzahl, T, VT, B, VB)

        liste.append(Nummer)
        

    liste.sort(key=attrgetter("FinalPunktzahl"), reverse=False)
 
    tabelle = "\n %20s \n %-10s %-15s %-30s\n" % (Altersklasse, "Platz", "Ergebnis", "Name")
    #tabelle = "\n %-15s %-20s %-30s" % ("Platz", "Ergebnis", "Name")

    i = 0
    z = 1
    PunktzahlAlt = None

    while liste != []:
        Objekt = liste.pop()
        Name = Objekt.Name
        FinalPunktzahl = Objekt.FinalPunktzahl
        Rohergebnis = Objekt.Rohergebnis

        if PunktzahlAlt == FinalPunktzahl:
            i += 0
            z += 1
            
        else:
            i += z
            z = 1
            
        PunktzahlAlt = FinalPunktzahl

        tabelle = tabelle + "\n %-10s %-15s %-30s" % (str(i), Rohergebnis, Name)

        
    LABEL.destroy()
    ROOT.update()
           



while True:
    for TabellenName in TabellenListe:
        TabellenBlatt = client.open(TabellenName).sheet1
        main()
    #TabellenBlatt = client.open("FinaleMannlich9").sheet1
    #main()