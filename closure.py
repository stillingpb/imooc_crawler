# coding=utf-8
def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print 'pass'
        else:
            print 'failed'
    return cmp

f100 = set_passline(60)
f150 = set_passline(90)

f100(59)
f100(89)

f150(59)
f150(89)