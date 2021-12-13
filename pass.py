import string, random

def passwordGenerator(totalLength):
    global wachtwoord, special_chars

    wachtwoord = []

    special_chars = "?_&%#@"
    hoofdletterA = random.randrange(2,6)
    randomNummer = random.randrange(4,7)
    kleineletterA = totalLength - (hoofdletterA + randomNummer + 3)

    wachtwoord += (random.choices(string.ascii_uppercase, k = hoofdletterA))
    wachtwoord += (random.choices(string.digits, k = randomNummer))
    wachtwoord += (random.choices(string.ascii_lowercase, k = kleineletterA))
    wachtwoord += (random.choices(special_chars, k = 3))
    random.shuffle(wachtwoord)
    eersteDrie()

def eersteDrie():
    for character in wachtwoord[:3]:
        if character.isnumeric():
            passwordGenerator(24)
    else:
        specialChars()

def specialChars():
    if wachtwoord[0] in special_chars and wachtwoord [-1] in special_chars:
        passwordGenerator(24)
    else:
        print(*wachtwoord, sep = "")

passwordGenerator(24)