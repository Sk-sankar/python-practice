
a=[2,3,4,5] 
a.insert(1,12)
print(a)

a=[3,2,4,2]
b=[6,5,7,4]
a.extend(b)
print(a)


def is_palindrome(s):
    reversed_s = s[::-1]  
    if s == reversed_s:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

# Test the function
is_palindrome("madam") 
is_palindrome("hello")  

#def palindrome(a):
  #  a=input("enter the value:").strip()
  #  b=list(a)
  #  c=[]
   # for i in range(len(b)-1,-1,-1):
 #       c.append(i)
  #  if(c==a):
 #       print("palindrome")        
 #   else:
 #       print("not palindrome")   

#palindrome(a)        


a=[1,2,3,4]
a.append(7)
a.pop(3)

print(a)
print(a[0])

b=(1,2,3)
c=list(b)
print(c)


d={1,2,3,2,4}
d.add(5)
print(d)


dic={
    "name":"sankar",
    "age":18,
    "place":"chennai"
}
dic.update({"phone":2879832119})

dic.pop("place")
print(dic.keys())
print(dic.values())
print(dic["name"])
del dic["age"]
print(dic)
dic.clear()
print(dic)
