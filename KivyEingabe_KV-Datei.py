from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


Builder.load_string("""
<MainButton>:
    Button:
        text: "Main"
        pos: root.right - self.width, root.height - self.height
        color: 0,1,0,1
        font_size: 20
        size: root.width, root.height
        on_press: funktion

<MainScreen>:
    FloatLayout
        MainButton
        
""")

#on_press: app.root.current = "menu"
def funktion():
    print("Das klappt")

class MainButton(Widget):
    pass

class MainScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name = "main"))


#Hauptklasse erstellen
class MainApp(App):
    def build(self):
        return sm

#Hauptprogramm starten
MainApp().run()