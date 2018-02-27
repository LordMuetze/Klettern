import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
TabellenListe = ["JgdDW"]
TabellenName = "JgdDW"

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.button import *
from kivy.uix.boxlayout import *


from functools import partial

x=0
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------


class Kletterer:
    def __init__(self, Vorname, Nachname, Startklasse, Zeile):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Name = Vorname + " " + Nachname
        self.VersuchListe = []
        self.V = 0
        self.VT = 0
        self.VB = 0
        self.T = 0
        self.B = 0
        self.V_ges = 0
        self.VT_ges = 0
        self.VB_ges = 0
        self.T_ges = 0
        self.B_ges = 0
        self.BonusSchonDa = False
        self.Ergebnis = "0T0 0B0"
        self.Zeile = Zeile
    
    def Versuch(self):
        self.VersuchListe.append("V")
    
    def Bonus(self):
        try:
            self.VersuchListe.pop()
        except:
            pass
        self.VersuchListe.append("B")

    def Top(self):
        try:
            self.VersuchListe.pop()
        except:
            pass
        self.VersuchListe.append("T")

    def Fertig(self):
        print(self.VersuchListe)
        
        while self.VersuchListe != []:
            
            try:
                self.Variable = self.VersuchListe.pop(0)
            except:
                pass



            if self.Variable == "V":
                self.V += 1



            elif self.Variable == "B":
                self.V += 1
                self.B += 1
                self.VB += self.V
                self.BonusSchonDa = True



            elif self.Variable == "T":
                self.V += 1
                self.T += 1
                self.VT += self.V


                if self.BonusSchonDa == False:
                    self.B += 1
                    self.VB += self.V
                


        self.Ergebnis = str(self.T) + "T" + str(self.VT) + " " + str(self.B) + "B" + str(self.VB)               
        print(self.Ergebnis)
        quit()



def Auswahl(instance):

    global x
    global Kletterer

    Vorname = TabellenBlatt.cell(x,1).value
    Nachname = TabellenBlatt.cell(x,2).value
    FinalPunktzahl = TabellenBlatt.cell(x,3).value
    T = TabellenBlatt.cell(x,4).value
    VT = TabellenBlatt.cell(x,5).value
    B = TabellenBlatt.cell(x,6).value
    VB = TabellenBlatt.cell(x,7).value
    Startklasse = TabellenBlatt.cell(1,1).value

    Kletterer = Kletterer(Vorname,Nachname,Startklasse,x)

    print("\n\n\n")

class AuswahlApp(App):

    def build(self):
        global TabellenBlatt
        global x

        Altersklasse = TabellenBlatt.cell(1,1).value

        AllesDatensaetze = TabellenBlatt.get_all_records()
        AnzahlZeilen = len(AllesDatensaetze) 

        layout = BoxLayout(orientation='vertical')

        x=2
       
        print("\n\n")
        while x <= AnzahlZeilen:

            x+=1
            
            Vorname = TabellenBlatt.cell(x,1).value
            Nachname = TabellenBlatt.cell(x,2).value

            print("btn" + str(x) + " = Button(text = Vorname + ' ' + Nachname)")
            exec("btn" + str(x) + " = Button(text = Vorname + ' ' + Nachname)")
            exec("btn" + str(x) + ".bind(on_press=Auswahl)")
            exec("layout.add_widget(btn" + str(x) + ")")
        
        print("\n\n")

        Back = Button(text="Fertig")
        Back.bind(on_press=quit)
        layout.add_widget(Back)

        return layout



class EingabeApp(App):

    def build(self):
        global TabellenBlatt

        layout = BoxLayout(orientation='vertical')

        btn1 = Button(text="Versuch")
        btn1.bind(on_press=Kletterer.Versuch)
        layout.add_widget(btn1)

        btn2 = Button(text="Bonus")
        btn2.bind(on_press=Kletterer.Bonus)
        layout.add_widget(btn2)

        btn3 = Button(text="Top")
        btn3.bind(on_press=Kletterer.Top)
        layout.add_widget(btn3)

        btn4 = Button(text="Fertig")
        btn4.bind(on_press=Kletterer.Fertig)
        layout.add_widget(btn4)

        return layout


# for TabellenName in TabellenListe:
#     print("Neuer Durchlauf")
TabellenBlatt = client.open(TabellenName).sheet1
#App().run()
if __name__ == '__main__':
    AuswahlApp().run()
    EingabeApp().run()