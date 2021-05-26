# A module for calculatin body mass index and body fat percentage

# Function definitions

# Body mass index
def bmi(weight, height):
    
    """Calculates the BMI

    Args:
        weight (float): weight (kg)
        height (float): height (cm)

    Returns:
        float: bmi
    """
    bmi = weight / (height/100) ** 2
    return bmi
    
# Fat percentage
def fat_percentage(bmi, age, sex):
    """Calculates the fat pecentage

    Args:
        bmi (float): body mass index
        age (float): age in years
        sex (int): 1 - Male, 0 - Female

    Returns:
        float: kehon rasvaprosentti
    """
    # F-% for adults
    if age >= 18:
        fat_percentage = 1.2 * bmi + 0.23 * age - 10.8 * sex - 5.4
    else:
        # F-% for children
        fat_percentage = 1.51 * bmi - 0.70 * age - 3.6 * sex + 1.4
    
    return fat_percentage

# Tests
if __name__ == '__main__':
    
    # 1. test, my bmi
    my_height = 171
    my_weight = 74.9
    my_bmi = bmi(my_weight, my_height)
    print('Pituus:', my_height, 'Paino:', my_weight, 'Painoindeksi', my_bmi) 

    # 2. test my fat
    my_age = 59
    my_sex = 1
    print('Rasvaprosentti:', fat_percentage(my_bmi, my_age, my_sex))