def decimal_to_roman(decimal):
    simbolos_1 = ['V', 'L', 'D']
    simbolos_3= ['I', 'X', 'C', 'M']
    if decimal <= 3:
        return decimal*'I'
    elif decimal == 4:
        return 'IV'
    elif decimal == 5:
        return 'V'
    elif decimal in {6,7,8} :
        return 'V'+((decimal-5)*'I')
    elif decimal == 9:
        return 'IX'
    elif 10<=(decimal)<=99:

        base = decimal//10 #1-9 / 0 - 90
        base_simbolo = ['X','XX','XXX','XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        desplazamiento = decimal - (base*10)
        desplazamiento_simbolo = ['','I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        romano = base_simbolo[base-1] + desplazamiento_simbolo[desplazamiento]

        return romano