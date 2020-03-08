import sys

VOWEL_LIST=["A", "E", "I", "O", "U"]
CLEANWORD =""

while True:
    CLEANWORD = input("Give us a word, or hit enter to exit: ")

    if CLEANWORD.lower() == "":
        break

    FIRSTLETTER = CLEANWORD[0]

    if FIRSTLETTER.upper() in VOWEL_LIST:

        PLWORD = CLEANWORD + "way"
    else:
        PLWORD= (CLEANWORD[1:]) + FIRSTLETTER + "ay"


    print("%s ==> %s" % (CLEANWORD,PLWORD))
