# 1 cast to integer type.
f = -1.6
print(int(f))
c = 2.99
print(int(c))

# 2 replace symbol.
s ='www.my.site.com#about'
s = s.replace('#','/')
print(s)

# 3 write a program that adds 'ing'
q = 'stroka'
b = q+'ing'
print(b)

# 4 swap words
s = 'Ivan Ivanou'
print(s[s.rfind(' ')+1:]+s[s.find(' '):s.rfind(' ')+1]+s[:s.find(' ')])

# 5 remove spaces at the beginning and end of a sentence
s = "' Hello_world. '"
x = "".join(s.split())
print(x)

# 6 Create a dictionary by linking it to the "school" variable and populate it with data reflecting the number of students
school = {"1a": "28", "1b": "30", "1d": "25", "2a": "32", "2b": "27", "6a": "30", "6b": "29","6d": "26", "7a": "21","7b": "31"}
print(school)
print(school["2a"])

# 7 create a list and extract the second element from it
l = ["apples", "bananas", "oranges", "carrots", "onions"]
print(l[1])

# 8 determine if line 1 is in line 2
