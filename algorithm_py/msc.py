def calculate(expression: str) -> int:
    # +12+2 = 3
    # (1+2)/3 = 1
    # ()->
    # */
    # +-
    # Rescursion -> evaluate each expression between ()
    # Within each (): parse the number -> process ops
    it = 0

    def calc() -> int:
        nonlocal it

        num = 0
        stack = []
        sign = "+"

        def evaluate_ops(num: int, op: str) -> None:
            nonlocal stack
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))

        while it < len(expression):
            if expression[it].isdigit():
                num = num * 10 + int(expression[it])
            elif expression[it] != "+-*/":
                # put things on stack
                evaluate_ops(num, sign)
                num = 0
                sign = expression[it]
            elif expression[it] == "(":
                it += 1
                # recursive call
                num = calc()
            elif expression[it] == ")":
                # inner recursive call
                evaluate_ops(num, sign)
                return sum(stack)
            it += 1
        evaluate_ops(num, sign)
        return sum(stack)

        return 0

    return 0
