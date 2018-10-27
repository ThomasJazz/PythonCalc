import math
from pythonds.basic.stack import Stack


def toPost(infix):
    # dictionary containing our math operation priorities according to PEMDAS
    priority = {
        "^": 4,
        "#": 4,  # this will be my representation of a square root
        "*": 3,
        "/": 3,
        "%": 3,
        "+": 2,
        "-": 2,
        "(": 1  # this isn't according to PEMDAS because they are used more as delimiters than operators
    }
    opStack = Stack()
    postList = []
    expression = infix.split()

    # check if our value is a number or parenthesis
    for val in expression:
        if val in "0123456789":
            postList.append(val)
        elif val == '(':
            opStack.push(val)
        elif val == ')':
            topToken = opStack.pop()

            while topToken != '(':
                postList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (priority[opStack.peek()] >= priority[val]):
                  postList.append(opStack.pop())
            opStack.push(val)

    while not opStack.isEmpty():
        postList.append(opStack.pop())
    return " ".join(postList)


def calcExpression(rawInput):

    i = count = 0
    left = right = operand = ""
    replaceStr = ""
    newStr = ""
    while i < len(expression) and len(expression) > 1:
        replaceStr += expression[i]

        if expression[i] == " ":
            count += 1

        if count == 0:
            left += str(expression[i])
        elif count == 1:
            right = str(expression[i])



        if isLegalOp(expression[i]):
            operand = expression[i]
            newStr = str(calculate(operand, left, right))
            expression = expression.replace(replaceStr, newStr)
            i = 0
            count = 0
            newStr = ""
            replaceStr = ""

        i += 1

    return expression


def calculate(operand, left, right):
    left = int(left)
    right = int(right)
    return {
        #'^': math.pow(left, right),
        '*': left * right,
        '/': left/right,
        '+': left+right,
        '-': left-right
    }[operand]


def isLegalOp(char):
    legalChars = "#%^*/+-"

    return char in legalChars


testDivides = "5 / 5 + 2 - 1"
postDivides = toPost(testDivides)
print(calcExpression(postDivides))

print(calcExpression("5 * 5"))
#print(calcExpression("( 5 + 5 ) ^ 2"))
print(calcExpression("5 * 9 + 3 / ( 8 + 4 )"))
