obj=open("D:\\CS\\story1.txt","r") //WHERE THE .txt FILE IS SAVED
s1=obj.read()
print(s1)

l=0
space=0
digi=0
symbol=0
vo=['a','e','i','o','u','A','E','I','O','U']
v=0
line=0
upper=0
lower=0
for a in s1:
    if a==' ':
        space=space+1

    if a.isdigit():
        digi=digi+1

    if not a.isalnum():
        symbol=symbol+1
        
    if a in vo:
        v=v+1
        
    if a =='\n':
        line=line+1

    if a.isupper():
        upper=upper+1

    if a.islower():
        lower=lower+1

        
    l=l+1


print("Total no of Characters: ",l)
print("Total no of Spaces:",space)
print("Total no of characters without spaces:",l-space)
print("Total no of digits:",digi)
print("Total no of Special Characters:",symbol)
print("Total no of Vowels:",v)
print("Total no of Lines:",line)
print("Total no of Uppercase Letters:",upper)
print("Total no of Lowercase Letters:",lower)
print("Total no of Consonents:", (upper+lower)-v)
obj.close()
