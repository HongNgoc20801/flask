from flask import Flask

app = Flask(__name__)


@app.route('/')
def randomapp():  # put application's code here
    print("Welcome to TLNY food")
    print("""How TLNY food help you?
             whether are you wondering about the food that you are going to enjoy with your family.
            """)
    print("Do you want TNLY FOOD help you to do that? ")
    choice = input()
    while True:
        if choice == "no":
            break
        elif choice == 'yes':
            print(" Have you had your own food?")
            ans = input()
            while True:
                if ans == 'yes':
                    print('Let me know which food that you are wondering')
                    import random
                    user_input = input("Enter a list of words separated by spaces \n "
                                       "Example: Bo_kho ca_chien Pho \n "
                                       "Please, enter ur list:")
                    words = user_input.split()
                    random_word = random.choice(words)
                    print("Random word:", random_word)
                    break
                elif ans == "No":
                    print("so sad")
                else:
                    break
            break


if __name__ == '__main__':
    app.run(port=5000, debug=True)