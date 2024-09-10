# https://www.scaler.com/topics/caesar-cipher-python/
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# ASCII
# Unicode
# chr
# ord
# print(chr(97))
# print(ord('a'))

# 97: a
# 65: A
# 97-122 -> 0-25
# Python strings are immutable
# Python lists are mutable

#right
# s= list(input())
# n = int(input())
# for i in range(len(s)):
#     char_ord = ord(s[i])
#     char_ord -= 97
#     char_ord += n
#     char_ord %= 26 #هی ان تا کم شود تا به بازه 0 تا 25برسیم
#     char_ord += 97
#     s[i] = chr(char_ord)
# s = ''.join(s)
# print(s)


#left
s= list(input())
n = int(input())
for i in range(len(s)):
    char_ord = ord(s[i])
    char_ord -= 97
    char_ord -= n
    char_ord %= 26 #هی ان تا کم شود تا به بازه 0 تا 25برسیم
    char_ord += 97
    s[i] = chr(char_ord)
s = '   '.join(s)
print(s)