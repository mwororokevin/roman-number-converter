import math

x = input("Enter a number a number greater than 0 but less than 5001: ")
number = int(x)

less_than_ten = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]

def roman_converter(number):
    roman_number = ""
            
    roman_number += thousands[math.floor(number / 1000)]
    number %= 1000
    roman_number += hundreds[math.floor(number / 100)]
    number %= 100
    roman_number += tens[math.floor(number / 10)]
    number %= 10
    roman_number += less_than_ten[math.floor(number)]
    
    return roman_number

print(roman_converter(number))

for i in range(0, 1000, 50):
    print(roman_converter(i))

