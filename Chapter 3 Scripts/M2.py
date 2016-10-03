# M2.py - Temperature Conversion Program: Addition of Kelvin Scale
#
# Modify the Temperature Conversion program in Figure 3-19 to add an additional
# option of converting to and from degrees Kelvin. The formula for conversion 
# to Kelvin (K) from Celsius (C) is K = C + 273.15.
#
# date:    10/02/2016
# author:  n/a
# license: n/a

# Temperature Conversion Program (Celsius-Fahrenheit-Kelvin)

def temp_convert(temp, base, target):
    g = { 'f' : (lambda f: (f + 459.67) * (5 / 9)), 
          'c' : (lambda c: c + 273.15), 'k' : (lambda k: k) }
    f = { 'f' : (lambda k: (k * (9 / 5)) - 459.67),
          'c' : (lambda k: k - 273.15), 'k' : (lambda k: k) }
    
    # function composition --> f(g(x))
    return f[target](g[base](float(temp)))

def main():
    # inits
    base = target = temp = None
    unit = { 'f' : "Fahrenheit", 'c' : "Celsius", 'k' : "Kelvin" }
    
    # helpers
    get_option = lambda string: string and string.lower()[0]
    is_invalid = lambda option: option not in ('f', 'c', 'k')
    
    # greet
    print('This program converts temperatures (Fahrenheit/Celsius/Kelven)')
    
    # from/to units to convert
    while is_invalid(base): 
        base = get_option(input("Enter base unit (f/c/k): "))
    while is_invalid(target):
        target = get_option(input("Enter target unit (f/c/k): "))

    # get the temperture
    # TODO: fix crash on carriage return when nothing is entered
    temp = input('Enter temperature to convert: ')
    while float(temp) < { 'f' : -459.67, 'c' : -273.15, 'k' : 0 }[base]:
        temp = input('Invalid, try again: ')
    
    # convert temp based upon base and target entered
    result = format(temp_convert(temp, base, target), '.1f')
    print(temp, "degress", unit[base], "is", 
          result, "degress", unit[target] + '.')

__name__ == "__main__" and main() or None
