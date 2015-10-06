#coding=utf-8
__author__ = 'xiyuanbupt'

a={'w':1,'xi':2}
print a
a.keys()
print a.values()
print a.keys()
print type(a.keys())
print a.items()
for item in a.iteritems():
    print item

print a.iteritems()
for key in a.iterkeys():
    print key

print a.iterkeys()
print a.pop('w')
print a
print a.values()
b={'w':3}
a.update(b)
print a
print a.viewitems()
print a.viewkeys()
print a.viewvalues()
a.viewkeys()
c=a.viewkeys()
print c
for item in c :
    print item

