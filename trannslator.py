#this code takes a word or sentenes from user 
#and turns vowel letter to z 

def translate (str):
    translation = ""
    for letter in str:
        if letter.lower()  in "aeoui":
            if letter.isupper() :
             translation = translation + "Z"
            else:
                translation = translation + "z"
        else:
           translation = translation + letter
    return translation

print(translate(input("enter name: ")))