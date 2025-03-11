time = 0
sentence = input("Input your sentence: ")
while True:
    if time < 11:
        time += 1
        before = input("Input the letter you want to change: ")
        after = input("Input the letter you want to change to: ")
        pos = sentence.find(before)
        if pos < 0:
            print("Letter not found")
            # stop the program
            break
        sentence = sentence.replace(before, after)
        con = input("Do you want to continue? y/n: ")
        if con == 'n':
            print(sentence)
            break
        print(f"Current sentence: {sentence}")
    else:
        print("You reach the limitation!")
        print(sentence)
        break
