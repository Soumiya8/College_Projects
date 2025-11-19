#simple Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "A"
            else:
                translation += "s"
        else:
            translation += letter
    return translation
        
phrase = input("Enter the Phrase: ")
print(translate(phrase))

