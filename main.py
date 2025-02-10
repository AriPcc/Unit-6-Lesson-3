def main():
    hobbies = []
    text = "Your favorite hobbies are "
    entry = " "

    print("Think of your favorite hobbies or activities.")
    while entry != "":
        if len(hobbies) == 0:
            entry = str(input("What's an activity you enjoy? "))
        else:
            entry = str(input("What's another activity you enjoy? "))
        # Remove extra whitespace and set to lower case
        entry = (" ".join(entry.split())).lower()
        # Avoid adding empty string to list
        if entry != "":
            hobbies.append(entry)
    
    # Grammar for at least 3 hobbies
    if len(hobbies) > 2:
        for i in range(len(hobbies)):
            if i < len(hobbies) - 1:
                text += hobbies[i] + ", "
            else:
                text += "and " + hobbies[i] + "."
    # Grammar for just 2 hobbies
    elif len(hobbies) == 2:
        text += hobbies[0] + " and " + hobbies[1] + "."
    # Grammar for only 1 hobby
    elif len(hobbies) == 1:
        text = "Your favorite hobby is " + hobbies[0] + "."
    # Grammar for no hobbies
    else:
        text = "You have no hobbies? That's kind of sad."
    
    print("\n", text)

main()