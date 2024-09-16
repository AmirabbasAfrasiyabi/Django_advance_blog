"""
    Given a string s containing just the characters
    '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

    Example 1:
        Input: s = "()"
        Output: true

    Example 2:
        Input: s = "()}"
        Output: false

    Example 3:
        Input: s = "{()}"
        Output: true

    Example 3:
        Input: s = "({)}"
        Output: false

    Constraints:
        1 <= s.length <= 10^6
        s consists of parentheses only '()[]{}'.
"""

s = list(input())
stack = []
is_valid = True
open_brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
}
for char in s:
    if char in ('(', '[', '{'):
        stack.append(char)
    elif len(stack) > 0 and stack[-1] == open_brackets[char]:
        stack.pop()
    else:
        is_valid = False
        break
if len(stack) > 0:
    is_valid = False
print('Yes' if is_valid else 'No')


