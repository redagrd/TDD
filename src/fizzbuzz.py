# def fizzbuzz(n):
#     """Transforme un entier en chaîne de caractères selon les règles du jeu fizzbuzz"""
#     if n == 9:
#         return "fizz"
#     elif n == 10:
#         return "buzz"
#     elif n == 15:
#         return "fizzbuzz"
#     elif n == 2:
#         return "2"
#     else:
#         return str(n)
    
def fizzbuzz(n):
    """Transforme un entier en chaîne de caractères selon les règles du jeu fizzbuzz"""
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

