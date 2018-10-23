import math

def inputParser(input):
    # if there are no parenthesis in the expression then we can just evaluate the entire expression at face value
    if "(" and ")" not in input:
        calcExpression(input)

    root = "sqrt"
    # check for sqrt function
    if root in input:
        slice = find_str(root, input+len(root))
        handleParen(input[slice:])

    # initial check to make there are no illegal characters or expressions
    leftParen = 0
    rightParen = 0
    for i in range(0, len(input)):
        if not(input[i].isDigit() or isLegalChar(input[i])):
            return False

        if input[i] == "(":
            leftParen += 1

        if input[i] == ")":
            if rightParen >= leftParen:
                return "Error, illegal use of ')'"
            rightParen += 1

    # if we have more of one type of parenthesis than the other
    if leftParen != rightParen:
        return "Illegal usage of parenthesis"

    for i in range(0, len(input)):
        inputRev = reversed(input)
        currChar = inputRev[i]

        if currChar == "(":
            tempRev = reverse(input[i:])
            j = 0
            while not(tempRev[j]==")"):
                j += 1

            replaceMe = input[i:len(input)-j-1]
            withMe = handleParen(input[i:len(input)-j-1])
            input.replace(replaceMe,withMe)

def handleParen(exp):
    output = ""

    for i in range (1, len(exp)):
        if exp[i] == ")":
            return calcExpression(output)
        elif exp[i] == "(":
            output += handleParen(exp[i:])
        else:
            output += exp[i]


def isLegalChar(char):
    legalChars = ".()^*/+-"

    return char in legalChars

# this will only be used for locating the sqrt function in an input string
def find_str(char, str):
    index = 0

    if char in str:
        c = char[0]
        for ch in str:
            if ch == c:
                if str[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
def reverse(str):
    rev = ''
    for i in range(len(str),0,-1):
        rev += str[i - 1]

    return rev

def calcExpression(expression):
    i = 0
    while i < len(expression):
        if i == len(expression):
            return expression

        if isLegalChar(expression[i]):
            if (i == len(expression)-1):
                return "Incorrect use of operand: " + expression[i]

            lOperand = ""
            for j in range(i-1,-1,-1):
                if expression[j].isdigit():
                    lOperand += expression[j]
                else:
                    break

            lOperand = reverse(lOperand)

            rOperand = ""
            for j in range(i+1, len(expression)):
                if expression[j].isdigit():
                    rOperand += expression[j]
                else:
                    break

            operation = expression[i]
            replaceMe = "" + lOperand + operation + rOperand
            withMe = str(calculate(operation,str(lOperand),str(rOperand)))
            expression = expression.replace(replaceMe, withMe)
            i = 0
            if expression == withMe:
                return withMe
        else:
            i += 1


    return expression

def calculate(operand, left, right):

    return {
        '^': math.pow(int(left),int(right)),
        '*': int(left) * int(right),
        '/': int(left)/int(right),
        '+': int(left)+int(right),
        '-': int(left)-int(right)
    }[operand]


print(calcExpression("5*5+2-3"))