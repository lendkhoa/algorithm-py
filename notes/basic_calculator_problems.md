# Basic Calculator Problems
⭐️ There are 4 basic operations (+, -, /, *). * and / take precedence <br>
⭐️ If the current operation is addition (+) or subtraction (-), then the expression is evaluated based on the precedence of the next operation. <br>
⭐️ The whitespaces between the characters <br>
 - 3+2 / 2
 - 3 + 2 / 2 are valid examples
 - isspace(), isdigit() Python

## Stack base
- Scan the string from left to right
- if current character is digit-> calculate the currentNumber.
- If not, the current character must be an operator. We evaluate the expression based on the type
	- if +, - we have to evaluate based on the last operator.
	- Stack (LIFO) stores the last expression
	- if *, / pop the value from the stack and evaluate
```py
class Solution:
    def calculate(self, expression: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        it = 0
        
        def update(op: str, v: int) -> None:
            nonlocal stack

            if op == "+":
                stack.append(v)
            if op == "-":
                stack.append(-v)
            if op == "*":
                stack.append(stack.pop() * v)
            if op == "/":
                stack.append(int(stack.pop() / v))

        num, stack, sign = 0, [], "+"

        while it < len(expression):
            if expression[it].isdigit():
                num = num * 10 + int(expression[it])
            elif expression[it] in "+-*/":
                update(sign, num)
                num, sign = 0, expression[it]
						# IF we don't have () we can remove this
            elif expression[it] == "(":
                it += 1
                num = calc()
            elif expression[it] == ")":
                update(sign, num)
                return sum(stack)
            it += 1
        update(sign, num)
        return sum(stack)
        
```

*Time and Space analysis*
- Time: O(n): n is the number of characters
- Space: O(n):

## Space optimized version

Instead of storing the evaluated expression in the stack. We could add the values to the result and keep track of the last calculated number<br>

If the operation is Multiplication (*) or Division (/), we must evaluate the expression lastNumber * currentNumber and update the lastNumber with the result of the expression. This would be added to the result after the entire string is scanned.<br>
```py
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        s += '+' # ❗️ important
        currentNumber = 0
        lastNumber = 0
        result = 0
        operation = '+'
        
        for currentChar in s:
            if currentChar.isdigit():
                currentNumber = (currentNumber * 10) + int(currentChar)
            else:
                if currentChar != ' ':
                    if operation == '+':
                        result += lastNumber
                        lastNumber = currentNumber
                    elif operation == '-':
                        result += lastNumber
                        lastNumber = -currentNumber
                    elif operation == '*':
                        lastNumber = lastNumber * currentNumber
                    elif operation == '/':
                        lastNumber = int(lastNumber / currentNumber)
                    
                    operation = currentChar
                    currentNumber = 0
        
        result += lastNumber
        return result
```
*Time and Space analysis*
- Time: O(n): n is the number of characters
- Space: O(1):