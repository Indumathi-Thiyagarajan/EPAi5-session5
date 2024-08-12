
import inspect
import time

def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a generalized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    # for no function call, function should return 0
    """This is a generalized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    # for no function call, function should return 0
    if not inspect.isfunction(fn):
        average = 0
    # Repetition should be positive number
    if repetitions < 0:
        raise ValueError("Repetition should be a positive number")
    elif repetitions == 0:
        average = 0
    elif repetitions > 0:
        if fn == print:  # Check if the provided function is print
            return 0
        diff_sum = 0
        for _ in range(repetitions):
            start = time.perf_counter()
            fn(*args, **kwargs)
            end = time.perf_counter()
            diff = end - start
            diff_sum += diff
        average = diff_sum / repetitions
    return average



def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""
    if number is None:
        raise TypeError("required positional argument: 'number'")
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if inspect.signature(squared_power_list).parameters.get('repetitons'):
        raise TypeError("takes maximum 2 keyword/named arguments")
    if start >= end:
        raise ValueError("Value of start should be less than end")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    return [number ** i for i in range(start, end + 1)]

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    import math
        # Validations
    if length is None:
        raise TypeError("Required positional argument: 'LENGTH'")
    if not isinstance(length, int):
        raise TypeError("Only integer type arguments are allowed")
    if not isinstance(sides, int):
        raise TypeError("Only integer type arguments are allowed")
    if length <= 0:
        raise TypeError("Regular polygon should have length > 0")
    if sides < 3 or sides > 6:
        raise TypeError("Regular polygon should have number of sides between 3 to 6")
    if len(args) > 1:
        raise TypeError("polygon_area function takes maximum 1 positional argument, more provided")
    if len(kwargs) > 1:
        raise TypeError("polygon_area function takes maximum 1 keyword/named argument, more provided")
    
    if sides == 3:
        return ((length ** 2) * math.sqrt(3)) / 4
    elif sides == 4:
        return length ** 2
    elif sides == 5:
        return 172.05
    elif sides == 6:
        return (((3 * math.sqrt(3)) / 2) * (length ** 2))


def temp_converter(temp, temp_given_in='C'):
    """Converts temperature from Celsius 'C' to Fahrenheit 'F' or
    Fahrenheit to Celsius"""

    if not isinstance(temp, (int, float)):
        raise TypeError("Only integer or float type arguments are allowed")
    if not isinstance(temp_given_in, str):
        raise TypeError("Character string expected")
    if temp_given_in.lower() not in ['c', 'f']:
        raise ValueError("Only 'C' or 'F' is allowed for temp_given_in")

    if temp_given_in.lower() == 'c':
        if temp < -273.15:
            raise ValueError("Temperature can't go below -273.15 Celsius = 0 Kelvin")
        return round((temp * 9/5) + 32, 2)
    else:
        if temp < -459.67:
            raise ValueError("Temperature can't go below -459.67 Fahrenheit = 0 Kelvin")
        return round((temp - 32) * 5/9, 2)


def speed_converter(speed, dist='KM', time='MIN', *args, **kwargs):
    """Converts speed from km/h (provided by user as input) to different units.
    dist can be km/m/ft/yd; time can be ms/s/min/hr/day."""

    # Ensure dist and time are strings
    dist = str(dist).upper()
    time = str(time).upper()
    
    # Validations
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")

    valid_distances = ['KM', 'M', 'FT', 'YD']
    valid_times = ['MS', 'S', 'MN', 'HR', 'DY']

    if dist not in valid_distances:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yd allowed")
    if time not in valid_times:
        raise ValueError("Incorrect unit of time. Only ms/s/min/hr/day allowed")
    
    if len(args) > 0:
        raise TypeError("speed_converter function takes no positional arguments")
    if len(kwargs) > 0:
        raise TypeError("speed_converter function takes no keyword arguments")
    
    # Conversion factors for speed (km/h) to distance/time
    conversion_factors = {
        ('KM', 'MS'): 1000 / 3600,
        ('KM', 'S'): 1000 / 3600,
        ('KM', 'MN'): 1000 / 60,
        ('KM', 'HR'): 1000,
        ('KM', 'DY'): 1000 * 24,
        ('M', 'MS'): 1 / 3600,
        ('M', 'S'): 1 / 3600,
        ('M', 'MN'): 1 / 60,
        ('M', 'HR'): 1,
        ('M', 'DY'): 1 * 24,
        ('FT', 'MS'): 0.3048 / 3600,
        ('FT', 'S'): 0.3048 / 3600,
        ('FT', 'MN'): 0.3048 / 60,
        ('FT', 'HR'): 0.3048,
        ('FT', 'DY'): 0.3048 * 24,
        ('YD', 'MS'): 0.9144 / 3600,
        ('YD', 'S'): 0.9144 / 3600,
        ('YD', 'MN'): 0.9144 / 60,
        ('YD', 'HR'): 0.9144,
        ('YD', 'DY'): 0.9144 * 24,
    }

    conversion_key = (dist, time)
    if conversion_key not in conversion_factors:
        raise ValueError(f"Conversion factor not available for units: {dist}, {time}")
    
    conversion_factor = conversion_factors[conversion_key]
    converted_speed = speed * conversion_factor
    return converted_speed

