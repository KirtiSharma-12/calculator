FirstNumber = float(input("Enter first number = "))
SecondNumber = float(input("Enter Second number = "))
opr = str(input("Enter your operation (+, -, *, /) = "))

if opr == "+":
    total = str(FirstNumber + SecondNumber)
elif opr == "-":
    total = str(FirstNumber - SecondNumber)
elif opr == "*":
    total = str(FirstNumber * SecondNumber)
elif opr == "/":
    total = str(FirstNumber / SecondNumber)
else:
    total = str("Unknown Operation Selected")

print(total)