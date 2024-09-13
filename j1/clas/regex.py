import re
import requests

# r = requests.get('https://quera.org/blog/')
# print(re.findall(r'<h4> <a href="(.*)">(.*)</a></h4>', r.text))

# txt = 'The rain in Spain'
# x = re.search(r'^The(.*)Spain$', txt)
# print(x.group(1))

s = """
ali@alavi.com
taghi@taghavi.com
naghi@naghavi.com
"""

# print(re.findall(r'.+(?=@)', s))
# # s = re.sub(r'.+(?=@)', '****', s)
# s = re.sub(r'.+(?=@)', lambda m: m.group()[::-1], s)
# print(s)

s = """
#ffdede
#dedede
#000000
#ffffff
#abacad
"""

print(re.findall(r'(#([0-9a-f]{2})\2{2,})', s))

# re.findall(pattern, string, flags=re.I|re.M|re.X)
# re.sub('[a-z]+@', 'ABC@', s)
# p = re.compile('[a-z]+@')
# p.sub('ABC@', s)
# re.sub('([a-z]+)@([a-z]+)', r'\2@\1', s)

# a = 'foo'
# b = 'bar'

# text = 'find a replacement for me [[:a:]] and [[:b:]]'

# desired_output = 'find a replacement for me foo and bar'

# def repl(m):
#     contents = m.group(1)
#     if contents == 'a':
#         return a
#     if contents == 'b':
#         return b

# print re.sub('\[\[:(.+?):\]\]', repl, text)
