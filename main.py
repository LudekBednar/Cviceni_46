def caesar(text,posun):
    mala = "abcdefghijklmnopqrstuvwxyz"
    velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zprava = ""
    for i in range(len(text)):
        if text[i].islower():
            abeceda = mala
        else:
            abeceda = velka
        index = abeceda.find(text[i])
        if text[i] == " ":
            zprava += " "
        elif index + posun >= len(abeceda):
            index_2 = index + posun - len(abeceda)
            zprava += abeceda[index_2]
        else:
            zprava += abeceda[index+posun]
    return zprava

    return zprava

message = 'abc def ghi jkl mno pqr stu vwx Yz'

print(caesar(message,2))
