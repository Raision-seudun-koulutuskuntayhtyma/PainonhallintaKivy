# PAINONHALLINTASOVELLUKSEN GRAAFINEN KÄYTTÖLIITTYMÄ

# Kirjastojen lataukset
import kivy

# Komponettien alustukset
from kivy.app import App
from kivy.core import text # Varsinaisen sovelluksen ikkuna
from kivy.uix.gridlayout import GridLayout #Asetteluruudukko
from kivy.uix.button import Button # Painike
from kivy.uix.textinput import TextInput # Tekstikenttä
from kivy.uix.label import Label # Kentän otsikko
 
# Sovelluksen alustukset ja luokkien määrittelyt

# Sijoitteluruudukko 2 saraketta, rivimäärää dynaaminen
class AppGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Asetetaan sarakemäärä
        self.cols = 2
        

        # Lisätään käyttöliittymän komponentit
        self.add_widget(Label(text='Etunimi')) # Otsikko etunimi
        self.first_name = TextInput() # Tekstikenttä etunimelle
        self.first_name.font_size = 16
        self.add_widget(self.first_name) # Lisätään kenttä käyttöliitymään
        
        self.add_widget(Label(text='Sukunimi'))
        self.last_name = TextInput()
        self.add_widget(self.last_name)

        self.add_widget(Label(text='Pituus (cm)'))
        self.person_height = TextInput()
        self.add_widget(self.person_height)

        self.add_widget(Label(text='Paino (kg)'))
        self.person_weight = TextInput()
        self.add_widget(self.person_weight)

        self.submit = Button(text='Laske')
        self.submit.font_size = 24
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.bmi = TextInput()
        self.bmi.disabled = True
        self.bmi.font_size = 24
        self.bmi.background_color = 'fcba03'
        self.bmi.foreground_color = 'fc030b'
        self.add_widget(self.bmi)

    # Painikkeen toiminnon määrittely
    def pressed(self, instance):
        p_height = float(self.person_height.text)
        p_weight = float(self.person_weight.text)
        p_bmi = p_weight / (p_height / 100)**2
        self.bmi.text = str(round(p_bmi))

# Luodaan varsinainen käyttöliittymän ikkuna
class WeightApp(App):
    def build(self):
        return AppGrid() # Ikkunan sisältönä AppGrid-luokka ja sen elementit


# Suoritetaan käyttöliitymä
if __name__ == "__main__":
    WeightApp().run()
   