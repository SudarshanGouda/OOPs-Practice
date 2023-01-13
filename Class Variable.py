
class User:

    next_id=1

    def __init__(self,name=''):
        self.name=name
        self.id=User.next_id
        User.next_id += 1


users=[ User() for _ in range (0,21)]

for user in users:
    print (user.id)
