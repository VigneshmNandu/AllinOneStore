

# def checkSubStingFound(subString, mainString):
#     """
#     this function checks if a subString is present in mainString
#     first if remove the special charaters then make both the strings to lower then checks if the subString is present in mainString
#     """

#     alphanumeric_MainString = ""
#     alphanumeric_subString = ""

#     # removing special charater from maniString
#     for character in mainString:
#         if character.isalnum():
#             alphanumeric_MainString += character

#     # removing special charater from subString
#     for character in subString:
#         if character.isalnum():
#             alphanumeric_subString += character

#     if alphanumeric_subString.lower() in alphanumeric_MainString.lower():
#         return True
#     else:
#         return False


def checkSubStingFound(search, title):
    # search = "Macbook pro M2"
    # title = "New Apple 13 Macbook Pro Gold- M1 chip (2020)"

    # Searchwords = search.lower().split(" ")
    # titleWord = title.lower().split(" ")

    # print(Searchwords)
    # print(titleWord)

    searchwords = search.lower().split(" ")
    titleWords = title.lower().split(" ")

    searchWords_in_title = all(item in titleWords for item in searchwords)

    if searchWords_in_title is True:
        return True
    else:
        return False


# print(checkSubStingFound("Macbook air m1", "Macbook Apple air gold M1"))

# search = "Asus vivobook"
# title = "Asus Pentium Quad Core - 4 Gb/1 Tb Hdd/Windows 10 Home X543ma-gq1020t Laptop"

# if checkSubStingFound(search, title):
#     print("it works")
# else:
#     print("not match")
