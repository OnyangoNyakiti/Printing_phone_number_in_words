phone_dictionary = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
phone_number = input("Enter your phone number: ")
output = ""
for phone in phone_number:
    output += phone_dictionary.get(phone, "") + " "
print(output)