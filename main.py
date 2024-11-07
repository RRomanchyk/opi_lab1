ope = input("Введіь оператор  (+ - * /): ")

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

if ope == "+":
    print(num1 + num2)
elif ope == "-":
    print(num1 - num2)
elif ope == "*":
    print(num1 * num2)
elif ope == "/":
    print(num1 / num2)
else:
    print("Такого оператору не існує")
