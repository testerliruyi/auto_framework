class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1


if __name__ == "__main__":
    a=Student('li')
    b=Student('ru')
    print(Student.count)


