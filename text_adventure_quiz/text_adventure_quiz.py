name = input("Hello what is your name?")
print(f"Welcome to the E-safety quiz {name}! You will be answering questions and only have 3 lives. if you answer a question incorrectly, you will lose a life. if you run out of lives, you lose.")
print("Are you ready?")
answer_1 = input()
if answer_1 == "yes":
    print("Lets go!")
else:
     print("Thats not an option!")
lives = 3 
print("Who can you share your passwords with?:")
answer_2 = input().lower()
if answer_2 == "nobody":
    print("Correct!")
else:
    print("Incorrect!")
    lives -= 1 
    print(f"You now have {lives} lives left")
print("You should never share your passwords with anyone as this can be very dangerous. People can impersonate you, you can get hacked, your data can be lost or leaked and your personal information will be breached.")
print("Next question!")
print("If you post something on the internet, who may be able to see it?")
answer_3 = input().lower()
if answer_3 == "everyone":
    print("Correct!")
else:
    print("Incorrect!")
    lives -= 1
    print(f"You now have {lives} lives left")
print("Unless you change your privacy settings, everyone will be able to view anything that you post, so be carefull what you are sharing on the internet.")
print("Next question!")
print("if a friend posts something of you or about you on the internet that you dont like, and they wont take it down because they think its funny, who should you speak to?")
answer_4 = input().lower()
if answer_4 == "an adult":
    print("Correct!")
else:
    print("Incorrect!")
    lives -= 1 
    print(f"You now have {lives} lives left")
print("You should always speak to a trusty adult if someone posts mean things about you. This is classed as cyberbullying.")
if lives > 0:
    print("Next question!")
    print("if a stranger on the internet asks for a photo of you, should you send it to them? Yes or No")
    answer_5 = input().lower()
    if answer_5 == "no":
        print("Correct!")
    else:
        print("Incorrect!")
        lives -= 1 
        print(f"You now have {lives} lives left")
        print("You should never send images of yourself to anyone that you do not know as they can use them for malicious purposes and use them against you. Make sure you tell an adult.")
if lives > 0:
    print("Next question!")
    print("Your friend wants to meet someone she met on the internet. Should you keep it a secret? Yes or No?")
    answer_6 = input().lower()
    if answer_6 == "no":
        print("Correct!")
    else:
        print("Incorrect!")
        lives -= 1 
        print(f"You now have {lives} lives left")
        print("You should not keep it a secret and tell an adult straight away as your friend may be at risk of a danger.")
if lives > 0:
    print("Next question!")
    print("When creating a new password, should you include your full name? Yes or No?")
    answer_7 = input().lower()
    if answer_7 == "no":
        print("Correct!")
    else:
        print("Incorect!")
        lives -= 1
        print(f"You now have {lives} lives left")
    print("You should not use your name as it is not a strong enough password option.")
if lives > 0:

    print("Next question")
    print("Who should you accept friend requests from online?")
    answer_8 = input().lower()
    if answer_8 == "people you know":
        print("Correct!")
    else:
        print("Incorrect!")
        lives -= 1 
        print(f"You now have {lives} lives left")
print("GAME OVER!")
if lives > 0:
    print("WELL DONE. YOU WON!")
else:
    print("Better luck next time :( ")


