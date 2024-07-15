## 1. time_it
### Description:
Measures the average execution time of a given function over a specified number of repetitions.

Parameters:

fn: Function to time.
repetitions (optional): Number of times to execute fn.
*args, **kwargs: Additional arguments to pass to fn.
Returns:
Average time taken for fn to execute over repetitions.

## 2. squared_power_list
### Description:
Generates a list of powers of a number from start to end.

Parameters:

number: Base number for calculations.
start (optional): Starting power (default: 0).
end (optional): Ending power (default: 5).
Returns:
List of number raised to powers from start to end.

## 3. polygon_area
### Description:
Calculates the area of a regular polygon based on its number of sides and side length.

Parameters:

length: Length of each side of the polygon.
sides: Number of sides of the polygon (must be between 3 and 6 inclusive).
Returns:
Area of the regular polygon.

## 4. temp_converter
### Description:
Converts temperature between Celsius and Fahrenheit.

Parameters:

temp: Temperature value to convert.
temp_given_in: Unit of the input temperature ('c' for Celsius, 'f' for Fahrenheit).
Returns:
Converted temperature value.

## 5. speed_converter
### Description:
Converts speed from kilometers per hour (kmph) to various other units.

Parameters:

speed: Speed value in kmph to convert.
dist: Distance unit for the output speed ('km', 'm', 'ft', 'yd').
time: Time unit for the output speed ('ms', 's', 'min', 'hr', 'day').
Returns:
Speed converted to the specified units.


## Testing Session
def test_session5_readme_exists():
    """ 
    Test function to see if the readme file exists
    """

def test_session5_readme_500_words():
    """ 
    Test function to see if the readme file has more than or equal to 500 words 
    """

def test_session5_readme_proper_description():
    """ 
    test function to see if all the functions are explained in the readme file
    """

def test_session5_readme_file_for_more_than_10_hashes():
    """ 
    test function to see if comments are added explaining the code
    """
  

def test_session5_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''


def test_session5_time_it_no_args():
    """ 
        Test time_it with no arguments"""


def test_session5_time_it_incorrect_pos_args():
    """ 
        Test time_it with non existing positional arguments"""
  


def test_session5_time_it_zero_rep():
    """ 
        Test time_it with zero repetation. Should return 0 avg time"""


####################### Validations for squared_power_list()####################

def test_session5_squared_power_list_no_args():
    """
        Test squared_power function for no mandatory positional arguments"""
  

def test_session5_squared_power_list_incorrect_pos_args():
    """
        Test squared_power_list function for incorrect values for positional arguments"""
  

def test_session5_squared_power_list_incorrect_start__end():
    """
        Test squared_power_list function for incorrect value to start keyword arguments"""

def test_session5_squared_power_list_number_gt_10():
    """
        Test squared_power_list function for number value greater than 10"""

def test_session5_squared_power_list_unwanted_args():
    """
        Test squared_power_list function for unwanted positional/keyword arguments"""
        
def test_session5_squared_power_list_output():
    """
        Test squared_power_list function for output with multiple inputs"""

####################### Validations for polygon_area()####################
def test_session5_polygon_area():
    """Test polygon_area function for no mandatory positional arguments"""

def test_session5_polygon_area_sides_values():
    """Test polygon_area function for permissible values for sides, check for 0, 1, 2, 7"""

def test_session5_polygon_area_length_values():
    """Test polygon_area function for permissible values for sides (len > 0)"""

def test_session5_polygon_area_unwanted_args():
        Test polygon_area function for unwanted positional/keyword arguments"""


####################### Validations for temp_converter()########################

def test_session5_temp_converter():
    """Test temp_converter function for no mandatory positional arguments"""
    
def test_session5_temp_converter_temp():
    """Test temp_converter function for incorrect values for positional argument temp (check for string AND imaginary input) """


def test_session5_temp_converter_temp_given_in():
    """ 
        Test temp_converter function for incorrect value to temp_given_in keyword argument"""

def test_session5_temp_converter_temp_values_in_celsius():
    """ 
        Test temp_converter function for permissible values for temprature in celsius"""

def test_session5_temp_converter_temp_values_in_fahrenheit():
    """ 
        Test temp_converter function for permissible values for temprature in fahrenheit"""

def test_session5_temp_converter_unwanted_args():
    """ 
        Test temp_converter function for unwanted positional/keyword arguments"""

def test_session5_temp_converter_output_in_fahrenheit():
    """ 
        Test temp_converter function for output with multiple inputs in fahrenheit"""

def test_session5_temp_converter_output_in_celsius():
    """ 
        Test temp_converter function for output with multiple inputs in celsius"""

####################### Validations for speed_converter()########################

def test_session5_speed_converter():
    """ 
        Test speed_converter function for no mandatory positional arguments"""

def test_session5_speed_converter_speed():
    """ 
        Test speed_converter function for incorrect values for positional argument temp"""

def test_session5_speed_converter_dist():
    """ 
        Test speed_converter function for incorrect type of value for dist keyword argument"""

def test_session5_speed_converter_time():
    """ 
        Test speed_converter function for incorrect type of value for time keyword argument"""

def test_session5_speed_converter_speed_allowed_values():
    """ 
        Test speed_converter function for permissible value for speed argument"""

def test_session5_speed_converter_time_allowed_values():
    """ 
        Test speed_converter function for permissible value for time keyword argument"""

def test_session5_speed_converter_dist_allowed_values():
    """ 
        Test speed_converter function for permissible value for dist keyword argument"""

def test_session5_speed_converter_unwanted_args():
    """ 
        Test speed_converter function for unwanted positional/keyword arguments"""

def test_session5_speed_converter_output_km_to():
    """ 
        Test speed_converter function for output with multiple inputs from km/(x), x can be ms/s/min/hr/day"""

def test_session5_speed_converter_output_m_to():
    """ 
        Test speed_converter function for output with multiple inputs from m/(x), x can be ms/s/min/hr/day"""

def test_session5_speed_converter_output_ft_to():
    """ 
        Test speed_converter function for output with multiple inputs from ft/(x), x can be ms/s/min/hr/day"""

def test_session5_speed_converter_output_yrd_to():
    """ 
        Test speed_converter function for output with multiple inputs from yrd/(x), x can be ms/s/min/hr/day"""
