# def sai():
#     print("hello rella")
# sai()
""" even numbers"""
# def sai(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# b=sai(12)
# c=sai(3)
# print(b)
# print(c)
"""default arguments"""
# def sai(age=21):
#     print(f"age of the sai :{age}")
    
# a=sai()
# b=sai(24)
"""position"""
# def sai(name,age):
#     print(f" name of he person is : {name} and it's age is :{age} ")
# a=sai("sai",24)
# b=sai(24,"rella")
"""key word argument"""
# def sai(name,age):
#     print(f" name of he person is : {name} and it's age is :{age} ")
# a=sai(name="sai",age=24)
# b=sai(age=24, name="sai")
""" *argus"""
# def sai(*name):
#     print(name)
# a=sai("sai","rella","kumar")
"""Mixing Normal Parameters with *args"""
# def sai(name,*food):
#     print(f" name of the person is :{name} and it likes {food}")
# a=sai("rella","biriyani","chiken","milk")
""" **kwargs"""
# def sai(**name):
#     print(f"detaile os the preson :{name}")
# a=sai(name="rella" ,age="21",hight="170")
"""Unpacking Dictionary into **kwargs"""
# def sai(name,hight,age):
#     print(f"detaile os the preson :{name} and hight {hight} an age is {age}")
# a={"name":"rella" ,"age":21, "hight":170}
# b=sai(**a)
"""🔹 Using *args and **kwargs Together
normal → *args → **kwargs
"""
# def sai(name,*age,**detals):
#     print("normal ",name)
#     print(" * args :" ,age)
#     print("**args :",detals)
# a=sai("rella sai kumar",21,32,"sai",32,person="sai",rool=23,hight=170)
"""*args and **kwargs"""
def sai(*args,**kwargs):
    print(" the *args are")
    for i in args:
        print(i)
    print(" the kwrqags are")
    for k,v in kwargs.items():
        print(f"{k}:{v}")
a=sai("rella sai kumar",21,32,"sai",32,person="sai",rool=23,hight=170)
     
    
    