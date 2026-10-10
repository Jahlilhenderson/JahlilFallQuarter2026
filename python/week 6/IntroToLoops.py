prompt = input("Do you want me to print the list again? Y/N")
geniuses = ("Jayden", "Dayyon", "Jahlil", "Caden", "Jeremy")
prompt = "Y"

while prompt == "Y":
    for genius in geniuses:
        print(genius)
    prompt = input("Do you want to print this list again? Y/N")