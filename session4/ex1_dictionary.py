dictionary={
    "happy":":)",
    "sad":":(",
    "excited":"^_^",
    "super excited":"^o^",
    "considered":"..."
}

while True:
    ppl = input("How do you feel? - ")
    if ppl in dictionary:
        print("Translate: ",dictionary[ppl])
    else:
        print("Not found")
        action = input("Contribute(Y/N)?").upper()
        if action == "Y" or action == "YES":
            trans = input("Translation: ")
            dictionary[ppl] = trans #add a new values into dict
        else:
            print("bye")
    break


