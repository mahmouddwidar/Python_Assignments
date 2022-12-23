#important sites
# [1]- Python Regex Cheatsheet => https://www.debuggex.com/cheatsheet/regex/python
# [2]- pythex => https://pythex.org/
# [3]- Regular Expression 101 => https://regex101.com/


# -------------------------------
# -------------95-102------------
# -------------------------------

# -------------------------------
# ---------Assignment-1----------
# -------------------------------


import re

my_string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

result = re.findall(r"(\w )", my_string)

print(result)



# -------------------------------
# ---------Assignment-2----------
# -------------------------------


import re

my_string = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

result = re.search( r"(L[A-z]+)", my_string)

print(result)



# -------------------------------
# ---------Assignment-3----------
# -------------------------------


import re

my_string1 = "+(0100) 600-1234"
my_string2 = "+(0100) 60-1234"
my_string3 = "(0100) 6000-1234"
my_string4 = "01006001234"
my_string5 = "0100 600 1234"
my_string6 = "(0100) 600-1"
my_string7 = "(0100) 600-12"


result1 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string1)
result2 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string2)
result3 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string3)
result4 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string4)
result5 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string5)
result6 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string6)
result7 = re.findall(r"\+?\(\d{4}\)\s\d+-\d{4}", my_string7)



print(result1)
# ['+(0100) 600-1234']
print(result2)
# ['+(0100) 60-1234']
print(result3)
# ['(0100) 6000-1234']
print(result4)
# []
print(result5)
# []
print(result6)
# []
print(result7)
# []


# -------------------------------
# ---------Assignment-4----------
# -------------------------------


import re

url1 = "http://www.elzero.org:8888/link.php"
url2 = "https://elzero.org:8888/link.php"
url3 = "http://www.elzero.com/link.py"
url4 = "https://elzero.com/link.py"
url5 = "http://www.elzero.net"
url6 = "https://elzero.net"

result1 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url1)
result2 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url2)
result3 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url3)
result4 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url4)
result5 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url5)
result6 = re.findall(r"https?://(www\.)?(\w+)\.(com|org):?(\d+)?(.+)", url6)


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)



# -------------------------------
# ---------Assignment-5----------
# -------------------------------


# Regular Expression to match => (http || https) by 5 methods.

# RegEx. 1 => https?
# RegEx. 2 => http\w?
# RegEx. 3 => http.?
# RegEx. 4 => http[a-z]?
# RegEx. 5 => http\S?

import re

my_string = "http || https || abcd || abcd"

result = re.findall(r"(https?)", my_string)

print(result)
#['http', 'https']