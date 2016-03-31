class Member:
    def __init__(self, name):
        self.name = name
        print "(init member, name=%s)," % (self.name),

    def say(self):
        print "my name is : %s," % (self.name),

    def __str__(self):
        return "name : %s, " % (self.name)


class Teacher(Member):
    def __init__(self, name, salary):
        Member.__init__(self, name)
        self.salary = salary
        print "salary: %s" % (self.salary)

    def say(self):
        Member.say(self)
        print "salary: %s" % (self.salary)


class Student(Member):
    def __init__(self, name, score):
        Member.__init__(self, name)
        self.score = score
        print "score: %s" % (self.score)

    def say(self):
        Member.say(self)
        print "score: %s" % (self.score)

    def __str__(self):
        return  Member.__str__(self) + "score: %s" % (self.score)


class StudentList:
    def __init__(self):
        self.list = []

    def add(self, val):
        self.list.append(val)
        return self

    def __getitem__(self, idx):
        return self.list[idx]


#t = Teacher('teacher', 1000)
s1 = Student('s1', 64)
s2 = Student('s2', 95)
li = StudentList()
li.add(s1).add(s2)
print li[0]
print li[1]