class One:
    def pt(self):
        print('From Class One')

class Second(One):
    def pt(self):
        print('From Class Second')

class Third(One):
    def pt(self):
        print('From Class Third')

class Fourth(Second,Third):
    pass

O=One()
S=Second()
T=Third()
F=Fourth()

F.pt()