import math


def calculate(s: str) -> int:
    """
    Basic calculator with no parenthesis.
    """
    num = 0
    presign = "+"
    stack = []
    for i in s + "/":
        if i.isdigit():
            num = 10 * num + int(i)
        elif i in "+-*/":
            if presign == "+":
                stack.append(num)
            elif presign == "-":
                stack.append(-num)
            elif presign == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(math.trunc(stack.pop() / num))
            presign = i
            num = 0
    return sum(stack)


def calculate_no_stack(s: str) -> int:
    print(f"Evaluate {s}\n")
    cur_res = 0
    res = 0
    num = 0
    presign = "+"

    for char in s + "+":
        if char.isdigit():
            num = 10 * num + int(char)
            print(f"isdigit {num} cur_res {cur_res} res {res}")
        elif char in "+-/*":
            if presign == "+":
                cur_res += num
                print(f"+ cur_res: {cur_res} res {res}")
            elif presign == "-":
                cur_res -= num
                print(f"- cur_res: {cur_res} res {res}")
            elif presign == "*":
                cur_res *= num
                print(f"* cur_res: {cur_res} res {res}")
            elif presign == "/":
                cur_res = int(cur_res / num)
                print(f"/ cur_res: {cur_res} res {res}")

            # if the chracter is "+" or "-", we do not need to worry about
            # the priority so that we can add the curr_res to the eventual res
            if char in "+-":
                res += cur_res
                cur_res = 0
            presign = char
            num = 0

    return res


def minRemoveToMakeValid(self, s: str) -> str:
    """
    Given a string s of '(' , ')' and lowercase English characters.
    Your task is to remove the minimum number of parentheses
    ( '(' or ')', in any positions ) so that the resulting parentheses
    string is valid and return any valid string.
    Time complexity is O(n)
    Memory complexity is O(n)
    """
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""
    while stack:
        s[stack.pop()] = ""
    return "".join(s)


def valid_abbreviated_strings(word: str, abbr: str) -> bool:
    """
    Complexity
    Time: O(n)
    Space: O(1)
    """
    p1 = p2 = 0
    while p1 < len(word) and p2 < len(abbr):
        if abbr[p2].isdigit():
            if abbr[p2] == "0":  # leading zeros are invalid
                return False
            shift = 0
            while p2 < len(abbr) and abbr[p2].isdigit():
                shift = (shift * 10) + int(abbr[p2])
                p2 += 1
            p1 += shift
        else:
            if word[p1] != abbr[p2]:
                return False
            p1 += 1
            p2 += 1
    return p1 == len(word) and p2 == len(abbr)


def validPalindrome(self, s: str) -> bool:
    """
    Check if the string is a valid palindrome with at most 1 delete
    Complexity:
    Time: O(2^n)
    """
    n = len(s)
    if n == 0 or n == 1:
        return True
    if n == 3:
        return s[0] == s[2]
    l = 0
    r = n - 1

    while l < r:
        if s[l] != s[r]:
            remove_l = self.is_palindrome(s, l + 1, r)
            remove_r = self.is_palindrome(s, l, r - 1)
            return remove_l or remove_r
        else:
            l += 1
            r -= 1

    return True


def is_palindrome(self, s: str, i: int, j: int) -> bool:
    """
    Complexity:
    Time: O(n/2) -> O(n)
    Space: O(1)
    """
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def parse_string_from_right(s: str) -> int:
    n = 0
    i = 0
    operand = 0
    for i in range(len(s) - 1, -1, -1):
        operand = 10**n * int(s[i]) + operand
        n += 1
    return operand


def parse_string_from_left(s: str) -> int:
    n = 0
    for i in range(len(s)):
        n = 10 * n + int(s[i])
    return n


def simplify_path(s: str) -> str:
    """
    We want to focus on ./ and .. (go to parent directory)
    """
    stack = []
    n = len(s)

    for token in s.split("/"):
        if token == ".":
            continue
        elif token == "..":
            if stack:
                stack.pop()
        else:
            # print(f"Adding: {token}")
            stack.append(token)
    return "/".join(stack)


def test_simplify_path():
    input_str = "/home///abc/cd../../"
    print(f"input: {input_str}")
    print(f"Simplified path: {simplify_path(input_str)}")


def reverse_digits(digits: int) -> int:
    """
    Time: O(n)
    """
    result, rem = 0, abs(digits)
    while rem:
        result = result * 10 + rem % 10
        rem //= 10
    return -result if digits < 0 else result


# print(parse_string_from_right("123"))
# print(parse_string_from_left("123"))
# calculate_no_stack("6-4*2")
# test_simplify_path()
print(reverse_digits(12345))
