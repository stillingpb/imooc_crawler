# coding=utf-8

class Parent:
    def __init__(self, name):
        self.name = name
        print 'init parent'

    def say(self):
        print 'say:' + self.name

    def hi(self):
        print 'hi'


class Son(Parent):
    def __init__(self):
        Parent.__init__(self,'par')
        self.name = 'son'
        print 'init son'

    def say(self):
        Parent.say(self)
        print 'say', self.name

    def hi(self):
        pass


son = Son()
son.say()
son.hi()
