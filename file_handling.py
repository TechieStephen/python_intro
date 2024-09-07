file = open("students.txt")
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()

student_records = file.readlines()
# for x in file:
#     print(x)


def grade(score, subject):
    if(score >= 70):
        print(subject , ": A")
        
    elif(score >= 60):
        print(subject ,"B")
        
    elif(score >= 50):
        print(subject ,"C")
        
    else:
        print(subject ,"F")
        
        
for student_record in student_records:
    
    x = student_record.split(" ")
    name = x[0]
    math = x[1]
    english = x[2]
    
    print("GRADE FOR: " + name )
    grade(int(math), "MATH")
    grade(int(english), "ENGLISH")


