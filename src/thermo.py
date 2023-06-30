
def thermo_us1(temp):
    for thermo in temp:
        if thermo in range[2,9,1]:
            return 1

def thermo_us2(n):
    if n is None:
        return 0
    
def thermo_us3(temp):
    if len(temp) > 100000:
        raise ValueError ("Too many values")
