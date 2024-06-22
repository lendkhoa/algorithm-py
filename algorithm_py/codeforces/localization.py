"""
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.
Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.
This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.
Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".
"""

"""
1) inp — For taking integer inputs.
2) inlt — For taking List inputs.
3) insr — For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
4) invr — For taking space seperated integer variable inputs.
"""
import sys

input = sys.stdin.read

# Read all input at once and split into lines
data = input().split()

# The first line should be the number of following lines
n = int(data[0])

# Iterate through the next n lines
for i in range(1, n + 1):
    s = data[i]
    if len(s) > 10:
        print(s[0] + str(len(s) - 2) + s[-1])
    else:
        print(s)
