lexicon = {

    "a": "аa",
    "b": "b",
    "c": "сc",
    "d": "d",
    "e": "eе",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "iі",
    "j": "jȷ",
    "k": "kк",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "oо",
    "p": "pр",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "xх",
    "y": "yу",
    "z": "z",
    "A": "AА",
    "B": "BВ",
    "C": "СC",
    "D": "D",
    "E": "EЕ",
    "F": "F",
    "G": "G",
    "H": "HН",
    "I": "IІ",
    "J": "J",
    "K": "KК",
    "L": "L",
    "M": "MМ",
    "N": "N",
    "O": "OО",
    "P": "PР",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "TТ",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "XХ",
    "Y": "Y",
    "Z": "Z"

}
import random
output = open("result.txt", "w+", encoding="utf-8")
result = ''
task = input("Provide a sting to spoof")
for i in range(0, len(task)):
    letter = lexicon.get(task[i])
    if letter == None:
        result += task[i]
        continue
    result += random.choice(letter)
output.write(result)

