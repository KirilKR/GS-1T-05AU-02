# Kiril Krushkov
# GS-1T-05AU-02
import os

spur = "ja"
while spur == "ja":
    print("1.	Bæta við nýjum í símaskránna. ")
    print("2.	Breyta upplýsingum í símaskránni. ")
    print("3.	Eyða upplýsingum / eyða línu úr símaskránni. ")
    print("4.	Prenta út alla símaskránna ein lína per notanda. ")
    print("5.	Leita að ákveðnu nafni og prenta upplýsingar um það nafn, sima og kennitölu. ")
    print("6.   Hætta í forritinu. ")

    spurning = input("Í hvaða lið viltu fara? ")

    if spurning == "1":
        nafn = input("sláðu hér inn nafn ")
        simanumer = input("sláðu inn símanúmerið ")
        kt = input("Sláðu inn kennitölu ")

        skra = open("Simaskra.txt", "a")  # opna skra og setja i append

        skra.write(nafn + " " + simanumer + " " + kt + ";")  # setja texta í skra með semi kommu

        skra.close()  # loka

        skra = open("simaskra.txt", "r")  # opna og lesa

        print(nafn,simanumer,kt, "Hefur verið bætt við skranna ")  # prenta

        skra.close()  # loka

    if spurning == "2":
            coname = input('Hvaða fyrirtæki þú vilt fjarlægja? ')  # company name
            f = open('codilist.txt', 'r')  # Upprunalega símanúmer skráningu
            f1 = open('codilist.tmp', 'a')  # opna tmp skrá

            for line in f:
                if line.strip() != coname.strip():
                    for line in f:
                        f1.write(line)
                    break  # Mun síðar skrifa yfir codilist.txt með tmp SKRÁ
                else:
                    f1.write(line)
            else:
                print('Villa: Það félag er ekki skráð.')
            f1.close()
            f.close()
            continue

    if spurning == "3":
        os.remove("Path/To/File.ext")
        print("Utskila!") #fjarlægja skrár

    if spurning == "4":
        skra = open("simaskra.txt", "r")

        innihald = skra.read().split(";")

        for x in innihald:
            print(x)

        skra.close() #muna símaskrá


    if spurning == "5":
        leita = input("hvaða nafni ertu að leita að? ")

        skra = open("simaskra.txt", "r")

        innihald = skra.read().split(";")

        skra.close()

        for x in innihald:
            for i in x:
                print(i)
            ord = x.split(" ")
            #if ord == leita:
#                print("eg er snillingur", ord())

    if spurning == "6":
        print("Takk fyrir!")
        break