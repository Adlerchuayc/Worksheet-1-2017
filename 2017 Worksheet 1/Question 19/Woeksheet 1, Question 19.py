phrase = input("Phrase to encode:" + "\n")
shift = int(input("Enter shift value:" + "\n"))
if shift > 26:
    shift = shift - 26
encoded_phrase = ""
small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
big   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for c in phrase:
    if c in big:
        INDEX = big.index(c) + shift
        if INDEX > 25:
            INDEX = INDEX - 26
        c = big[INDEX]
    elif c in small:
        index = small.index(c) + shift
        if index > 25:
            index = index - 26
        c = small[index]
    encoded_phrase = encoded_phrase + c
print(encoded_phrase)
