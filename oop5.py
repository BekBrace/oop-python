# Polymorphism
# You have a method that has the same name, 
# but it can acct differently or returns differents results.

class CAT:
    def speak(self):
        return "MEOW!"
    
class ROBOT:
    def speak(self):
        return "BING!"
    
class DOG:
    def speak(self):
        return "WUUF!"

friends = [CAT(), ROBOT(), DOG()]
for friend in friends:
    print(friend.speak())
    

