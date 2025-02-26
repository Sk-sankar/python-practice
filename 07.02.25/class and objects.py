class students:
    total1=500 # static for all students

    def __init__(self,name,tamil,eng,math,sci,sco): #constructor
        self.Name=name
        self.Tamil=tamil
        self.English=eng
        self.Maths=math
        self.Science=sci
        self.Social=sco

    def total(self):
         
        add=self.Tamil+self.English+self.Maths+self.Science+self.Social

        if add>400:
            print("You were passed in A class ",add)
            print(f'{self.Name} total mark is {add}/{students.total1}')


student1=students("sankar",90,99,89,88,92)

student1.total()
print("All the students should get 400 out of",students.total1)


  
