"""
Expression s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
Input: s = "3+2*2"
Output: 7
Input: s = " 3+5 / 2 "
Output: 5
"""


def basic_cal_II_no_stack(s: str) -> int:
    return calculate_no_stack(s)


def calculate_no_stack(s: str) -> int:
    """
    Processing the expression from LEFT --> RIGHT
    Time complexity: O(n)
    Space complexity: O(1)
    """
    cur_res = 0
    res = 0
    num = 0
    presign = "+"
    for char in s + "+":
        print(f"Current: {char} | cur_res: {cur_res}")
        if char.isdigit():
            num = 10 * num + int(char)
            print(f"  isdigit {num} cur_res {cur_res} res {res}")
        elif char in "+-/*":
            if presign == "+":
                cur_res += num
                print(f" + cur_res: {cur_res} res {res}")
            elif presign == "-":
                cur_res -= num
                print(f"- cur_res: {cur_res} res {res}")
            elif presign == "*":
                cur_res *= num
                print(f" * cur_res: {cur_res} res {res}")
            elif presign == "/":
                cur_res = int(cur_res / num)
                print(f" / cur_res: {cur_res} res {res}")

            # if the chracter is "+" or "-", we do not need to worry about
            # the priority so that we can add the curr_res to the eventual res
            if char in "+-":
                print(f"⭐️ Add the current res: {cur_res} to stack")
                res += cur_res
                cur_res = 0
            presign = char
            num = 0

    return res


"""
Evaluate expressions:
Input: s = "1 + 1"
Output: 2
Input: s = " 2-1 + 2 "
Output: 3
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

 0 + 1 + 1
 Stack should only contain number, whenerver we encounter a notion, we have to evaluate the expression
"""


def calculate(expression: str):
    """
    Time: O(n)
    Space: O(n)
    """
    it = 0

    def calc() -> int:
        nonlocal it

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
        print(f"calc() is called | num: {num}, stack: {stack}, sign: {sign}")

        while it < len(expression):
            print(f"  current iterator {it}: {expression[it]}")
            if expression[it].isdigit():
                num = num * 10 + int(expression[it])
            elif expression[it] in "+-*/":
                update(sign, num)
                num, sign = 0, expression[it]
            elif expression[it] == "(":
                it += 1
                num = calc()
            elif expression[it] == ")":
                update(sign, num)
                return sum(stack)
            it += 1
        update(sign, num)
        return sum(stack)

    return calc()


def test_bc_II():
    # print(f'[BC 2] Expression 3/2: {basic_cal_II_no_stack("3/2")}')
    print(f'[BC 2] Expression  3+5 / 2 : {basic_cal_II_no_stack(" 3+5 / 2 ")}')


def test_calc():
    print(
        f'\n [pattern] Expression 2*(5+5*2)/3+(6/2+8): {calculate("2*(5+5*2)/3+(6/2+8)")}'
    )
    print(f'\n [pattern] Expression 3+5 / 2: {calculate("3+5 / 2")}')


# test_bc_II()
test_calc()
