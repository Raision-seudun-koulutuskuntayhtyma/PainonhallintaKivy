# WEIGHT MANAGEMENT APPLICATION MAIN 

# Libraries and modules
import kivy # The Kivy framework
kivy.require('2.0.0') # Minimum version of the framework
from kivy.app import App # A parent class for the main window
from kivy.uix.gridlayout import GridLayout # A parent class for the layout

# Initializations and class definitions

# The layout
class Glayout(GridLayout):
     
    # Functional parts ie methods
    def calculate_bmi(self): # Calculates Body Mass Index
        pass

    def calulate_fat(self): # Calculates the Fat percentage
        pass

# Create the app
class WeightManagementApp(App):
    def build(self):
        return Glayout()
        
# Run the app
if __name__ == "__main__":
   # Create the application object 
   weightManagementApp = WeightManagementApp()

   # Run it continuously
   weightManagementApp.run()