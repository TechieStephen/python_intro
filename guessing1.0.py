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
user_answer = input("Your Answer: ")

if(user_answer.lower() == answer.lower()):
    print("YEEEEEEH You are correct")
else:
    print("OPPS!! you are wrong")
    print("Correct: " + answer)
