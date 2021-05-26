# WEIGHT MANAGEMENT APPLICATION MAIN BOX LAYOUT

# Libraries and modules
import calculations
import kivy # The Kivy framework
kivy.require('2.0.0') # Minimum version of the framework
from kivy.app import App # A parent class for the main window
from kivy.uix.boxlayout import BoxLayout # A parent class for the layout

# Initializations and class definitions

# The layout
class BLayout(BoxLayout):
     
    # Functional parts ie methods
    def calculate_bmi(self): # Calculates Body Mass Index
        person_height = float(self.height_value.text) / 100
        person_weight = float(self.weight_value.text) 
        person_bmi = round(person_weight / person_height ** 2)
        self.bmi_value.text = str(person_bmi)

    def calculate_fat(self): # Calculates the Fat percentage
        person_age = float(self.age_value.text)
        person_sex = float(self.sex_value.text)
        person_bmi = float(self.bmi_value.text)
        person_fat = round(calculations.fat_percentage(person_bmi, person_age, person_sex))
        self.fat_value.text = str(person_fat)

# Create the app
class FatManagementApp(App):
    def build(self):
        return BLayout()
        
# Run the app
if __name__ == "__main__":

    # Create the application object 
    fatManagementApp = FatManagementApp()

    # Run it continuously
    fatManagementApp.run()