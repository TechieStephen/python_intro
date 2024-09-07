# understanding the problem
#Gusessing game
#store the question is asked
#answers to the question is provided
#A person guess the answer to the question
#we compare the person's answer to the supplied answer
#ifboth answers are the same then the person id correct 
#else the person is wrong

question = "I am something when you break me water comes out, WHAT AM I?"
answer = "Coconut"
print("Welcomne To GUESS GUESS")
print(question)

life = 3
while( life !=0 ):
    user_answer = input("Your Answer: ")

    if(user_answer.lower() == answer.lower()):
        print("YEEEEEEH You are correct")
    else:
        life = life - 1
        if(life > 0 ):
            print("OPPS!! you are wrong, try again")
        else:
            print("OPPS!! THE END")
        
    