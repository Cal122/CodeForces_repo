string = input()

string = string.replace("WUB", " ")
string = string.replace("  ", " ")
string = string.removeprefix(" ")

print(string)