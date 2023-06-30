from src.fizzbuzz import fizzbuzz

def test_fizzbuzz_us1():
    rst = fizzbuzz(9)
    assert rst == "fizz"

def test_fizzbuzz_us2():
    rst = fizzbuzz(10)
    assert rst == "buzz"

def test_fizzbuzz_us3():
    rst = fizzbuzz(15)
    assert rst == "fizzbuzz"

def test_fizzbuzz_us4():
    rst = fizzbuzz(2)
    assert rst == "2"

def test_fizzbuzz_us5():
    resultat_attendu = [
        "1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz",
        "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz",
        "fizz", "22", "23", "fizz", "buzz", "26", "fizz", "28", "29", "fizzbuzz",
        "31", "32", "fizz", "34", "buzz", "fizz", "37", "38", "fizz", "buzz",
        "41", "fizz", "43", "44", "fizzbuzz", "46", "47", "fizz", "49", "buzz",
        "fizz", "52", "53", "fizz", "buzz", "56", "fizz", "58", "59", "fizzbuzz",
        "61", "62", "fizz", "64", "buzz", "fizz", "67", "68", "fizz", "buzz",
        "71", "fizz", "73", "74", "fizzbuzz", "76", "77", "fizz", "79", "buzz",
        "fizz", "82", "83", "fizz", "buzz", "86", "fizz", "88", "89", "fizzbuzz",
        "91", "92", "fizz", "94", "buzz", "fizz", "97", "98", "fizz", "buzz"
    ]
    resultat = [calculer(n) for n in range(1, 101)]
    assert resultat == resultat_attendu

# def test_fizzbuzz_us5():
#     """Teste la fonction fizzbuzz"""
#     for i in range(1, 101):
#         rst = fizzbuzz(i)
#         if i % 3 == 0 and i % 5 == 0:
#             assert rst == "fizzbuzz"
#         elif i % 3 == 0:
#             assert rst == "fizz"
#         elif i % 5 == 0:
#             assert rst == "buzz"
#         else:
#             assert rst == str(i)
