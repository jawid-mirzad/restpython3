
# Syftet med det här programet är att ge kontakt information till de som söker.
import csv #Här laddar vi ner csv moduln.
print("Hej och välkommen till kontakt information")# Här skrivar ut en meddelande när proogrammet startas.

Val = True # Här har vi en variabel som vi behöver använda i while loopet.
Val1 = 0  #Här har en variabel som vi behöver i våran while loop.

while Val: #Här har vi en while loop. så länge loopet är True skrivar ut den som är i loopet. 
           #Inne i input har vi dictionary som innehåller 0 ,1,2,3,4
    Val1 = input(''' 
      Förname  [0]
      Eftername  [1]
      Gmail        [2]
      Mobilnummet    [3] 
      Födesldag         [4]
      Välj en av talet !''')
    if Val1 >= "5":  # Här har vi en alltarnativ om användaren skrivar ett tal som inte finns.
        print("Välj ett tal mellan 0 till 5") # användaren får meddelanda att välja ett tal mellan 0 till 5.

    if Val1 == "0": # Om val1 är lika med 0 då printas allt som är under if vilkort.
        with open("information.csv" , "r") as csv_file: # Öppnar vi csv filen som vi har i läsa mod eller read mod.
            csv_reader = csv.reader(csv_file) # Här har vi en variabel som är lika med csv.reader för att kunna läsa filen.
            for line in csv_reader: # Här har vi for loop som läsar filen rad på rad.
                print(line[0]) #Nu printas 0s innehåll.
            # Här nera har vi en variabel som innehåller en input som vi frågar användare om de vill sluta eller förtsätta med programmet.
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n": # Om användaren väljar n då stängs programmet. Om y då förtsättas programmet.
                Val = False # vårt while stängs. 

    elif Val1 == "1":  # Samma funktion som ovanför if villkoret fast med olika output.
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[1])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

 
    elif Val1 == "2":  # Samma funktion som ovanför if villkoret fast med olika output.
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[2])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

    elif Val1 == "3":  # Samma funktion som ovanför if villkoret fast med olika output.
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[3])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False

    elif Val1 == "4":  # Samma funktion som ovanför if villkoret fast med olika output.
        with open("information.csv" , "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line[4])
            val2 = input('''Vill du avsluta eller förtsätta:
            n för avsluta [n]
            y för förtsätta [y]''')
            if val2 == "n":
                Val = False
