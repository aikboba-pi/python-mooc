# Write your solution here
filename = "diary.txt"

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = input("Function: ")

    if choice == "1":
        entry = input("Diary entry: ")
        with open(filename, "a") as file:
            file.write(entry + "\n")
        print("Diary saved\n")

    elif choice == "2":
        print("Entries:")
        try:
            with open(filename, "r") as file:
                content = file.read()
                if content:
                    print(content, end="")
        except FileNotFoundError:
            pass

    elif choice == "0":
        print("Bye now!")
        break