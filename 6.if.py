"""Check Positive or Negative
Write a program to check if a number entered by the user is positive, negative, or zero."""
# a=int(input("ente the number :"))
# print("positive" if a>0 else "zero" if a==0 else "negative" )
"""Odd or Even
Take an integer from the user and check if it is odd or even."""
# a=int(input(" enter the number :"))
# print("even" if a%2==0 else "odd")
"""Voting Eligibility
Input age and check if the person is eligible to vote (age ≥ 18)."""
# a=int(input(" enter the age of the person"))
# print("eligible" if a>=18 else "not")
"""Maximum of Two Numbers
Take two numbers and print which one is greater."""
# a= int(input(" enter hte number"))
# b= int(input(" enter hte number"))
# print("a is max" if a>b else "equal" if a==b else " b is max")
"""Largest of Three Numbers
Write a program to find the largest of three numbers using if-elif-else."""
# a= int(input(" enter the number :"))
# b= int(input(" enter the number :"))
# c= int(input(" enter the number :"))
# print("a is large" if a>b and a>c else "b is large" if b>c else "equal" if a==b==c else "c is larger")
"""Leap Year Check
Check if a given year is a leap year or not.
👉 Hint: A year is leap if divisible by 4, but not by 100, except if also divisible by 400."""
# a=int(input(" enter the year"))
# if a%4==0 and a%100!=0:
#     print(" a is leap year")
# elif a%4==0 and a%100==0  and a%400==0:
#     print("leap year")
# else:
#     print(" this is not lleap year")
# """another type"""
# a=int(input(" enter the year"))
# print("leap year by 4 and 400" if a%400==0 else " notleap year by 100" if a%100==0 else "leap year by 4" if a%4==0 else "not by4" )
"""Calculator (if-elif-else)
Take two numbers and an operator (+,-,*,/) from the user and perform the calculation."""
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=input(" enter the oparetorsa like +,*,/,- :")
# print(f"addtion is{a+b}" if c=="+" else f"substracction is:{a-b} " if c=="-" else f"multiplactionis {a*b}" if c=="*" else f"division is {a/b}" if c=="/" else "enter the correcct op" )
"""Character Type Check
Input a character and check whether it is a vowel, consonant, digit, or special character."""
# a="@"
# b="a","e","i","o","u"
# if type(a)==int:
#     print(" yes its ")
# elif type(a)==str:
#    if a in b:
#     print(" yse vowels")
#    elif a.isalpha():
#        print("constants")
#    else :
#     print(" specal characters")
"""another"""
# a=input("enter the number")
# b=("a","e","i","o","u")
# if len(a)==1:
#    if "0"<=a<="9":
#        print(" yes digit")
#    elif a in b:
#     print(" yse vowels")
#    elif a.isalpha():
#        print("constants")
#    else :
#     print(" specal characters")
# else:
#     print("enter the single char")
"""Grade Calculator (Advanced)
Input student marks and print grades:

90+ → A

75-89 → B

50-74 → C

< 50 → Fail
"""
# a=int(input("enter the marks :"))
# print("a" if a>=90 else "b" if 75 <= a <= 85 else "c"  if 50<=a>=74 else "fail")
"""Login System (Nested if)
Create a program that asks for username & password.

If username is correct, check password.

If both match → "Login Successful".

Otherwise → "Invalid username/password"."""
print("login syastem")
a=input("enter the user name :")
us="saikumar03"
ps="Sai123@#"
if a==us:
    b=input(" enter the password :")
    if b==ps:
        print("login success")
    else:
        print("worng password")
else:
    print("wrong user name")