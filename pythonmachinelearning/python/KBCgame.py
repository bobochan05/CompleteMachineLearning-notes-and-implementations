#WAP to display programs like KBC
#use list data type to store the questions and their correct answers 
#display the final amount the person is winning 


print("Welcome to the KBC Game!")
question1 = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the boiling point of water?"
]


print("Here is the first question:")
print(question1[0])
print("Your options are:" 
      "\n1. amsterdam"
      "\n2. Paris" 
      "\n2. mumbai" 
      "\n3. London" 
)
input1 = input("Enter your answer in option 1, 2, 3, 4: ")
if input1=="2":
    print("Correct! You win $1000.")
else:
    print("Wrong answer! The correct answer is Paris.")
    print("You win $0.")



    print("Here is the second question:")
print(question1[1])
print("Your options are:" 
      "\n1. earth"
      "\n2. jupiter" 
      "\n2. venus" 
      "\n3. mars" 
)
input1 = input("Enter your answer in option 1, 2, 3, 4: ")
if input1=="2":
    print("Correct! You win $2000.")
else:
    print("Wrong answer! The correct answer is jupiter.")
    print("You win $0.")







