def calculateNric ( nric , arrayNric , tuple , arrayProducts, refTable) :
    #Storing individual digit
    for char in nric[0:7] :
        arrayNric.append(char) 
    
    #storing the result of multiplication
    for a ,b in zip(arrayNric , tuple ) :
        arrayProducts.append(int(a)*int(b))

    #Calulating ref no.
    totalProduct = sum(arrayProducts)
    if nric[7].upper() in "TG" :
        totalProduct = totalProduct +4
    remainer = totalProduct%11
    checkDigit = 11-remainer

    #validate if alphabet is correct
    if  nric[7].capitalize() == refTable[checkDigit-1] :
        officialRef = refTable[checkDigit-1]
    
    else :
        officialRef = "Invalid"

    return officialRef
    

def validateNric( msgString ) :
    #declaring unchange variable
    weight = (2, 7, 6, 5, 4, 3, 2)
    refTable = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "Z", "J")
    
    #loop till correct input
    while True :
        nricArray = []
        arrayProducts = []
        nric = input(msgString)
        
        #reject invalid first char
        if not nric[0].capitalize() in "SGT":
            print("First character must be S , T or G")

        #reject non 7 digits
        elif any(not char.isdigit() for char in nric[1:8]) :
            print("Invalid Input , NRIC must start with S or T followed by 7 digit.")
        
        #go to calulation for ref char
        else : 
            ref = calculateNric(nric[1:9], nricArray, weight, arrayProducts, refTable)
            if ref == "Invalid" :
                print("Invalid Input. NRIC reference character is invalid.")
            
           #if all condition meets
            else :
                print("Valid NRIC")
                print("---------------------------")
                print("Official Reference :", ref)   
                break   

validateNric("Enter NRIC: ")