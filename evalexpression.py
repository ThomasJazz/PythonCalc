from __future__ import division  # without this, eval wont do integer division properly
import sys
import math

def evalexpression(text):
    # surround the evaluation in a try block so we make sure there are no errors passed through
    try:
        output = ""
        val = eval(text)
        if not(text == '0') and not(isinstance(val, tuple)):
            output = eval(text)
        else:
            output = "0"
    except NameError:
        output = "Illegal Characters"
    except (SyntaxError, AttributeError):
        output = "Syntax Error"
    except TypeError:
        output = "Illegal Expression"
    except ZeroDivisionError:
        output = "Cannot Divide by 0"
    except ValueError:
        output = "No Solution"

    return output


var = str(sys.argv[1])

print(evalexpression(var))