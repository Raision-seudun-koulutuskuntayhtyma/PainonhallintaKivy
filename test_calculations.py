# Tests for module calculations.py

# Import module to be tested
import calculations

# Tests for bmi function 
def test_bmi():
    assert round(calculations.bmi(75, 171)) == 26

def test_adult_female():
    assert round(calculations.fat_percentage(26, 59, 0)) == 39

def test_adult_male():
    assert round(calculations.fat_percentage(26, 59, 1)) == 29

def test_child_female():
    assert round(calculations.fat_percentage(21, 17, 0)) == 21

def test_child_male():
    assert round(calculations.fat_percentage(21, 17, 1)) == 18