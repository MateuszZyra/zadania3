import sys
def main():
    def zad1():
        tekst = input("Napisz tekst:")
        slowa = tekst.split()
        slowa = len(slowa)
        print("Ilość słów to: " + str(slowa))

    def zad2():
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
        c = int(sys.stdin.readline())

        dzialanie = pow(a, b) + c

        print(dzialanie)

    def zad3():
        slowo = input("Podaj słowo: ")
        n = len(slowo)
        i = 0
        while i < n:
            if slowo[i] != slowo[n-1]:
                print("Nie")
            i += 1
            n -= 1
        print("Tak")

    def zad4():
        a = int(input("Podaj liczbe: "))
        if a == 2:
            print("Pierwsza")
        if a % 2 == 0 or a <= 1:
            print("Nie pierwsza")

        pierw = int(a**0.5) + 1
        for dzielnik in range(3, pierw, 2):
            if a % dzielnik == 0:
                print("Nie pierwsza")
        print("Pierwsza")

    def zad5():
        n = 2

    #zad1()
    #zad2()
    #zad3()
    #zad4()

main()