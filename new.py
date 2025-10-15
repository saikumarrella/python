# n=int(input(" enterr the nummber :"))
# count=0
# for i in range(2,n+1):

#     for j in range(2,i):
#         if i%j==0 :
#             break

#     else:
#             print(i)
#             count+=1
# print(count)
# def spy(n):
#    sum=0
#    mul=1
#    while n>0:
#       num=n%10
#       n= n//10
#       sum+=num
#       mul*=num
#    if sum==mul:
#       return True
# for i in range(100,999):
#    if spy(i)==True:
#       print(i)

# def numbers(n):
#     print(n)
#     if n==1:
#         return 1

#     return  numbers(n-1)
# a=numbers(10)

# def number(n):
#     if n==1:
#         return [1]

#     b=number(n-1)
#     b.append(n)
#     return b
# a=number(5)
# print(a)
"""even or odd numbers"""


# def even(n):
#     if n <= 25:
#         if n % 2 == 0:
#             print(f"{n} is even")
#         else:
#            print(f"{n} is odd")
           
#         odd(n + 1)


# def odd(n):
#     if n <= 25:
#         if n % 2 == 0:
#             print(f"{n} is even")
#         else:
#            print(f"{n} is odd")
#         even(n + 1)
# a = even(1)
# def main_menu():
#       n=int(input("enter the number 1 to go to sub menu and anyting is exit"))
#       if n==1:
#          sub_menu()
#       else:
#         print("exit")
# def sub_menu():
   
#       n=int(input("enter the number 0 to go to sub menu and anyting is exit"))
#       if n==0:
#          main_menu()
#       else:
#          print("exit")
# a=main_menu()


# a="saikumar"
# for i in range(len(a)):
#    print(a[i],i)

a=["sai" ,"kumar","rella","sunil","sai"]
start=0
for i,j in enumerate(a):
   # print(i,j)
  
   for k,l in enumerate(j,start):
      print(k,l)
      start+=1
      

