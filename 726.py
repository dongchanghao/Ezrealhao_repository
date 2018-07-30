import sqlite3
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.course)
if __name__ == "__main__":
    student1 = Student('zhangming',20,[69,88,100])
    print(student1.get_name(),student1.get_age(),student1.get_course())

class DictClass:
    def __init__(self,dict):
        self.dict = dict
    def del_key(self,key):
        del self.dict[key]
        return self.dict
    def get_dict(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return "not found"
    def get_key(self):
        return self.dict.keys()
    def update_dict(self,second_dict):
        return list(self.dict.values())+list(second_dict.values())
d = DictClass({'1':'2','2':'3','3':'4','4':'5'})
print(d.get_dict('4'))
print(d.del_key('4'))
print(d.get_dict('6'))
#print(d.get_dict('4'))
#print(d.update_dict({'a':'b'}))