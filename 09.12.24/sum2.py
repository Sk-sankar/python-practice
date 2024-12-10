class grandpa():
    def phone(self):
        print("grandpa's phone")
class dad(grandpa):
    def money(self):
        print("dad's money")  
class son(dad,grandpa):
    def lap(self):
        time="11.00"
        print("son's lap") 
        print("time:",time)


so=son()

so.lap() 
  