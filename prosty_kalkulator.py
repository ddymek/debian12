def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie dzielimy przez zero!!."


while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Podaj numer operacji (1/2/3/4/5): ")

    if wybor == '5':
        print("Kalkulator zakończył działanie.")
        break

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print("Wynik dodawania:", dodawanie(liczba1, liczba2))
        elif wybor == '2':
            print("Wynik odejmowania:", odejmowanie(liczba1, liczba2))
        elif wybor == '3':
            print("Wynik mnożenia:", mnozenie(liczba1, liczba2))
        elif wybor == '4':
            print("Wynik dzielenia:", dzielenie(liczba1, liczba2))
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
