# Write your solution here
filename = "dictionary.txt"

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")

    if choice == "1":
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        
        with open(filename, "a") as file:
            file.write(f"{finnish};{english}\n")
            
        print("Dictionary entry added")

    elif choice == "2":
        search_term = input("Search term: ")
        
        try:
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        fin, eng = line.split(";")
                        if search_term in fin or search_term in eng:
                            print(f"{fin} - {eng}")
        except FileNotFoundError:
            pass

    elif choice == "3":
        print("Bye!")
        break