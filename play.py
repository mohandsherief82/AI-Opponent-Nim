from nim import train, play

ai = train(100000)
while True:
    play(ai)
    again = (input("wanna play again? (Y/N)")).capitalize()
    if again == "Y":
        continue
    else:
        break
