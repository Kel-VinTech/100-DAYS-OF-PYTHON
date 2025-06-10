"""
Learning about object oriented programming
# it takes attributes and functions
"""

class User:


    """ initializing an object using the init
    """
    
    def __init__(self,username):
        # use the dot notation to create an attribute for it's object.
        self.username = username
        self.follower = 0
        self.following = 0
    def follow(self, user):
        user.following += 1
        self.following += 1


user_1 = User("David")
user_2 = User("Angel")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
