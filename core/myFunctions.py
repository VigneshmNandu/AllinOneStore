

def checkSubStingFound(subString, mainString):
    """
    this function checks if a subString is present in mainString
    first if remove the special charaters then make both the strings to lower then checks if the subString is present in mainString
    """

    alphanumeric_MainString = ""
    alphanumeric_subString = ""

    # removing special charater from maniString
    for character in mainString:
        if character.isalnum():
            alphanumeric_MainString += character

    # removing special charater from subString
    for character in subString:
        if character.isalnum():
            alphanumeric_subString += character

    if alphanumeric_subString.lower() in alphanumeric_MainString.lower():
        return True
    else:
        return False


# search = "Asus vivobook"
# title = "Asus Pentium Quad Core - 4 Gb/1 Tb Hdd/Windows 10 Home X543ma-gq1020t Laptop"

# if checkSubStingFound(search, title):
#     print("it works")
# else:
#     print("not match")
