class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for item in equation:
        if item == "(":
            stack.push(item)
        elif item == ")":
            if stack.size() == 0:
                return False
            stack.pop()
        else:
            continue
    return stack.size() == 0

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
print ("Pass" if not (equation_checker(')(((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
print ("Pass" if not (equation_checker(')(((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
print ("Pass" if not (equation_checker('()((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
