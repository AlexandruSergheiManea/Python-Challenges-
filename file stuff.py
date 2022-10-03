file = open("data.txt", "a+")


def prepend(text):
    file.write(text + "\n")
    file.close()


prepend(input(""))

