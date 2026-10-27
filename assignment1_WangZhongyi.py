# Name: [Wang Zhongyi]
# Assignment One

#Task 1
from turtle import*

speed(10)
bgcolor("black")
pensize(2) #Define the pensize

colors = ["red","orange","yellow","green","cyan","purple"]

penup()
goto(-100, 50) #Move the pen to the target pixel
pendown()
for i in range(60):
    pencolor(colors[i%6])

    forward(i*5)

    left(145)

penup()
goto(0,0)

pendown()

for i in range(30):
    pencolor(colors[i%6])
    forward(i*4)
    left(120 +2)

#Task 2
print("Question Answering Bot")
question = input("Ask me something: ")
if question == "HKU":
    print("Bot: HKU is a The University of Hong Kong.")
elif question == "robot":
    print("Bot: A robot is an automated machine .")
elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer.")
elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")
elif question == "human":
    print("Bot: Humans are creative.")
else:
    print("Bot: Sorry, I don't understand.")

#Task 3
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")
if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")
