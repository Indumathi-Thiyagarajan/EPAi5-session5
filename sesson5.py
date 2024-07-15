
import time
import inspect

def time_it(fn, *args, repetitons= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    # for no function call, function should return 0
    if inspect.isfunction(fn) == False:
        average = 0
    # Repetition should be positive number
    if repetitons < 0:
        return ValueError("Repetition should be positive number")
    elif repetitons ==0:
        average = 0
    elif repetitons > 0:
        diff_sum = 0
        for _ in range(repetitons):
            start = time.perf_counter()
            fn(*args,**kwargs)
            end = time.perf_counter()
            diff = end - start
            diff_sum+= diff
        average = diff_sum / repetitons
    return average


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""
    if number is None:
        raise TypeError("required positional argument: 'number'")
    if not isinstance(number, int):
        raise TypeError(" Only integer type arguments are allowed ")
    if start <0 or end <0:
        raise ValueError("Value of start or end can't be negative")
    if squared_power_list.__code__.co_argcount >1:
        raise TypeError("takes maximum 1 positional argument")
    if start> end:
        raise ValueError("Value of start should be less than end")
    if number>10:
        raise ValueError("Value of number should be less than 10")
    # Get the signature of the function
    sig = inspect.signature(squared_power_list)
    # Count the number of parameters that have a default value
    if len([param for param in sig.parameters.values() if param.default != inspect.Parameter.empty])>2:
        raise TypeError("takes maximum 2 keyword/named arguments")
    # Validations "if" block
    if start is None:
        start = 0
    if end is None:
        end = 5
    # Return the list of number to the power of numbers from start to end
    powered_list = list(map(lambda x: number**x, range(start,end+1)))
    # print(powered_list)
    return powered_list

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    # Validations
    import math

    if length is None:
        raise TypeError("required positional argument: 'LENGTH'")
    
    if not isinstance(length,int):
        raise TypeError("Only integer type arguments are allowed")
    
    if not length >0:
        raise TypeError("regular polygon should have length > 0")
    
    if len(args) > 1:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 1:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
 
    if sides >=3 and sides <=6:
        # Return area
        area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    else:
        return ValueError("Sides should be within 3 to 6")
    return area

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    temp_given_in = temp_given_in.upper()
    # Validations

    if not isinstance(temp, int):
        raise ValueError("Only integer type arguments are allowed")
    if not temp_given_in is 'F' or 'C':
        raise ValueError("Only F or C is allowed")
    
    # Test temp_converter function for permissible values for temprature in fahrenheit
    if temp_given_in =='F' and temp < -459.67:
        raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")

    # Test temp_converter function for permissible values for temprature in celsius
    if temp_given_in =='C' and temp < -273.15:
        raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
    
    if len(args) > 1:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 1:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in =='F':
        temperature = ((temp - 32) * 5 ) / 9

    if temp_given_in == 'C':
        temperature = ((temp * (9/5))+32)
    return temperature

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 299792.458:
        raise ValueError("Speed can't be greater than speed of light")

    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")

    dist = dist.lower()
    time = time.lower()

    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowe")

    if not isinstance(time, str):
        raise TypeError("Charcater string expected")
    
    if len(args) > 1:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 2:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    
    # Conversion factors for distance
    distance_conversion = {
        'km': 1,
        'm': 1000,
        'ft': 3280.84,
        'yd': 1093.61
    }
    
    # Conversion factors for time
    time_conversion = {
        'ms': 3600000,
        's': 3600,
        'min': 60,
        'hr': 1,
        'day': 1/24
    }
    
    if dist not in distance_conversion:
        raise ValueError(f"Invalid distance unit. Choose from: {list(distance_conversion.keys())}")
    
    if time not in time_conversion:
        raise ValueError(f"Invalid time unit. Choose from: {list(time_conversion.keys())}")
    
    # Convert km/h to the specified units
    speed_in_specified_units = speed * (distance_conversion[dist] / time_conversion[time])
    return speed_in_specified_units
