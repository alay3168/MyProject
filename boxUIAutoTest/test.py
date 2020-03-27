from BoxWebAutoTest.pageManager import BasePage
class a:
    sss=333
    def aa(self):
        a ='aa'
        print(a)

class b(a):
    b ="bb"
    print(b)
    print(a.sss)
    def bb(self):
        print(a.aa(self))

# class c(BasePage):
#     c = 'cc'

b()