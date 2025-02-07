class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_score(self):
        return self.score

class course:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,student):
            self.students.append(student)
         
    def get_avg(self):
         value=0
         for student in self.students:
              value+=student.get_score
              return value/len(self.students)     
         
        
   

s1=student("hari",19,90)
s2=student("bala",19,95)

course1=course("science",2)
course1.add_student(s1)
course1.add_student(s2)

print(course1.get_avg())


        