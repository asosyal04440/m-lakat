yükseklik=int(input("sayı gir"))
genişlik=int(input("sayı gir"))

for i in range(yükseklik):
    if i == 0 or i ==yükseklik-1:

        print("*"*genişlik)
    else:
        print("*"+" "*(genişlik-2)+"*")
        

    
    