"""
*****
*****
*****
*****
*****"""
# for i in range(5):
    # for i in range(5):
    #    print("*", end="")
    # print("")
"""
* 
* * 
* * *
* * * *
* * * * *"""
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
"""
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5"""
# n=5
# for i in range(n):
#     for j in range(1,i+2):
#         print(j, end=" ")
#     print()
"""
1
22
333
4444
55555"""
# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()
"""
* * * * * 
* * * * 
* * *
* *
*
"""
"""one"""
# n=5
# for i in range(5):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
"""two"""
# n=5
# for i in range(n):
#     for  j in range(n,i,-1):
#         print("*",end=" ")
#     print()
"""
12345
2345
345
45
5
n=5"""
# for i in range(n):
#     for j in range(i,n):
#         print(j+1,end="")
#     print()
'''
1 2 3 4 5 
1 2 3 4 
1 2 3
1 2
1
'''
# n=5
# for i in range(n):
#     for j in range(1,(n+1)-i):
#         print(j,end=" ")
#     print()
"""
          * 
        * * 
      * * *
    * * * *
  * * * * *
"""
"""normal"""
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
"""tekeu"""
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
"""
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
# n=5
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#      print("*",end=" ")
#     print()
"""takeu"""
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range((2*i)+1):
#         print("*",end=" ")
#     print()
"""
* * * * * * * * * 
  * * * * * * * 
    * * * * *
      * * *
        *
"""
"""normal"""
# n=5
# for i  in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
    # print()
""" takeu"""
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range((2*n)-(2*(i)+1)):
#         print("*",end=" ")
#     print()
"""
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
# n=5
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#      print("*",end=" ")
#     print()
# for i  in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     for j in range(n-i-2):
#         print("*",end=" ")
#     print()
"""takeu"""
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range((2*i)+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range((2*n)-(2*(i)+3)):
#         print("*",end=" ")
#     print()
""" 
* 
* * 
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()
"""
1 
0 1 
1 0 1
0 1 0 1
1 0 1 0 1
"""
# n=5
# for i in range(n):
#   if i%2==0:
#     start=0
#   else:
#     start=1
#   for j in range(i+1):
#     start=1-start
#     print(start,end=" ")
#   print()
"""
1             1 
1 2         2 1 
1 2 3     3 2 1
1 2 3 4 4 3 2 1

"""
# n=4
# for i in range(n):
#   for j in range(1,i+2):
#     print(j,end=" ")
#   for j in range((2*n)-2*(i+1)):
#     print(" ",end=" ")
#   for j in range(i+1,0,-1):
#     print(j,end=" ")
    
#   print()
"""
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
"""
# n=5
# num=0
# for i in range(n):
#   for j in range(i+1):
#     num+=1
#     print(num,end=" ")
#   print()
"""
a 
a b 
a b c
a b c d
a b c d e
"""
# a="abcde"
# n=5
# for i in range(n):
#   for j in range(i+1):
#     print(a[j],end=" ")
#   print()
"""
abcde
abcd
abc
ab
a
"""
# a="abcde"
# n=5
# for i in range(n):
#   for j in range(n-i):
#     print(a[j],end="")
#   print()
"""
a 
b b 
c c c
d d d d
e e e e e
"""
# a="abcde"
# n=5
# for i in range(n):
#   for j in range(i+1):
#     print(a[i],end=" ")
#   print()
"""
      a 
    a b a 
  a b c b a
a b c d c b a
"""
# a="abcde"
# n=4
# for i in range(n):
#   for j in range(n-1-i):
#     print(" ",end=" ")
#   for j in range(i+1):
#     print(a[j],end=" ")
#   for j in range(i*1,0,-1):
#     print(a[j-1],end=" ")
#   print()
"""
e 
d e 
c d e
b c d e
a b c d e
"""
# a="abcde"
# n=5
# for i in range(n):
#   for j in range(i+1,0,-1):
#     print(a[4-(j-1)], end=" ")
#   print()
"""
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""
# n=5
# for i in range(5):
#   for j in range(n-i):
#     print("*",end=" ")
#   for j in range(2*i):
#     print(" ",end=" ")
#   for j in range(n-i):
#     print("*",end=" ")
#   print()
# for i in range(5):
#     for j in range(i+1):
#       print("*",end=" ")
#     for j in range((2*n)-2*(i+1)):
#       print(" ",end=" ")
#     for j in range(i+1):
#       print("*",end=" ")
      
#     print()
"""
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * *
* *             * *
*                 *
"""
# n=5
# for i in range(5):
#     for j in range(i+1):
#       print("*",end=" ")
#     for j in range((2*n)-2*(i+1)):
#       print(" ",end=" ")
#     for j in range(i+1):
#       print("*",end=" ")
      
#     print()
# n=4
# for i in range(4):
#   for j in range(n-i):
#     print("*",end=" ")
#   for j in range(2+(2*i)):
#     print(" ",end=" ")
#   for j in range(n-i):
#     print("*",end=" ")
#   print()
"""
* * * * 
*     * 
*     *
* * * *
"""
# n=4
# for i in range(n):
  
#    for j in range(n):
#       if i==0 or i==3:
#         value="*"
#       elif j==0 or j==3 :
#         value="*"
#       else:
#         value=" "
#       print(value,end=" ")
#    print()
"""
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4
"""
n=7
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      value=4
    elif (i==1)or (i==n-2) or (j==1) or j==n-2:
        value=3
    elif (i==2)or (i==n-3) or (j==2) or j==n-3:
        value=2
    else:
      value="1"
    print(value,end=" ")
    
  print()