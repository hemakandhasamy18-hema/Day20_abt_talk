# ==========================================
# DAY 20 - EXPRESSION ENGINES
# Reverse Polish Notation (RPN) Evaluator
# ==========================================

def evaluate_rpn(tokens):
    stack = []

    for token in tokens:

        if token.lstrip("-").isdigit():
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack[-1]


# Get input from user
expression = input("Enter RPN expression: ")

# Convert input into tokens
tokens = expression.split()

# Evaluate expression
result = evaluate_rpn(tokens)

print("======================================")
print("       RPN EXPRESSION EVALUATOR")
print("======================================")
print("Expression:", tokens)
print("Result:", result)