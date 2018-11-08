fs = raw_input("Za fibornacijev niz ukucajte f, a za savrsen broj s.")
if fs != "f" and fs != "s":
    print ("Pogresan unos, molimo unesite malo slovo f ili s!")
else:
    if fs == "f":
        fib = input("Do kog broja zelite niz?")
        #print (f)
        f1 = 1
        f2 = 0
        ff = 0
        for r in range(0, fib):
            print ff,
            ff = f1 + f2
            f1 = f2
            f2 = ff
    elif fs == "s":
        k = int(input("Do kog broja zelis izracun?"))
        r = 0
        i = 0
        print (k)
        for z in range(1, k+1):
            for i in range(1, z):
                if (z % i) == 0:
                    r = r + i
            if z == r:
                print (z),
