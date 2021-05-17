# PAINONHALLINTASOVELLUKSEN GRAAFINEN KÄYTTÖLIITTYMÄ -PÄÄOHJELMA
"""This is the main program file for the weight management
application. This version uses a separate kv file to assign properties
for the graphical user interface. These properties are defined in the
kvweight.kv file. While the name of main application class is KvweightApp
the kv file must have the sama name, but without word App. 
kv file names shoud allways be written in lower case. 
"""

# Kirjastojen lataukset
import kivy
kivy.require('2.0.0') # Edellytetään vähintään 2.0 versiota

# Komponettien alustukset (Kivyn luokkien käyttöönotto)
from kivy.app import App # Varsinaisen sovelluksen ikkuna
from kivy.uix.gridlayout import GridLayout #Asetteluruudukko

 
# Sovelluksen alustukset ja luokkien määrittelyt

# Sijoitteluruudukko, ulkoasu määritelty kvweight.kv-tiedostossa
class Glayout(GridLayout):

    # Metodi painoindeksin laskemiseksi, kytketty painikkeeseen bmi_button
    def calculate_bmi(self):
        person_weight = float(self.weight_text.text) # kv-tiedoston id weight_text
        person_height = float(self.height_text.text) / 100 # kv-tiedoston id height_text
        person_bmi = round(person_weight / person_height**2, 1)
        self.bmi_text.text = str(person_bmi) # kv-tiedoston id bmi_text

    # TODO: Metodi, joka laskee rasvaprosentin

# Varsinainen sovellus, joka näyttää sijoitteluruudukon Glayout
class KvweightApp(App):
    def build(self):
        return Glayout()

# Sovelluksen käynnistys, mikäli tätä tiedostoa ajetaan suoraan        
if __name__ == "__main__":
    # Luodaan luokasta sovellus ja käynnistetään se, sen voi myös käynnistää suoraan luokasta.
    kvweightApp = KvweightApp()
    kvweightApp.run()  