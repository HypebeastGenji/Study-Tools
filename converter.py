import string 
flashcards = {"front": "back"}

translated = []

mode_add = True
cards = {"Cards": []}

def main(mode, letters=False):

    mode_add = mode
    while mode_add == True:

        num = int(input("Enter Num: "))
        def add_cards(num=num):

            card = []

            for i in range(num):
                word = input(str("Enter answer: "))
                uri_ext = "}}"
                front_end = "{{c1::"
                word = front_end + word + uri_ext
                card.append(word)
            cards["Cards"].append(card)
        add_cards()

        print(cards)
        def tranform(cards):
            card_list = cards["Cards"]
            for card in card_list:
                count = 0
                print("------------------")
                for data in card:
                    count += 1
                    if letters == False:
                        print(str(count) + ". " + data)
                    else:
                        print(string.ascii_uppercase[count-1] + ". " + data)


        add_again = input("Add another?: ")
        if add_again in ["y", ' ', '', 'yes']:
            mode_add = True
            print(cards)
            tranform(cards)
            continue
        elif add_again == "no" or "n":
            mode_add == False
            print(cards)
            tranform(cards)
            break
        else:
            tranform(cards)
            break

def start():
    main(mode_add, letters=True)

start()
