with open("text.txt", "r") as file:
    print(file.name)
    for i in range(0,2):
        FileContent=file.readline()
        print(FileContent)
