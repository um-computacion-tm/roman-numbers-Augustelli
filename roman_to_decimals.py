
def roman_to_decimals(romano : str ):
    romans_decimal = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    decimal = 0

    for i in range(len(romano)):
        if i+1 == len(romano):
            decimal = decimal + romans_decimal[romano[i]]
        elif romans_decimal[romano[i]] >= romans_decimal[romano[i+1]]:
            decimal =  decimal + romans_decimal[romano[i]]
        elif romans_decimal[romano[i]] < romans_decimal[romano[i+1]]:
            decimal = decimal - romans_decimal[romano[i]]
    
    return decimal


if __name__ == "__main__":
    pass