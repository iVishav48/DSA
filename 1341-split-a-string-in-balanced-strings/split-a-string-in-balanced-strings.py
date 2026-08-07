class Solution(object):
    def balancedStringSplit(self, s):
        match = 0 
        character = 0 
        for i in s:
            if i == "R":
                character +=1
            if i == "L":
                character -=1 
            if character == 0:
                match +=1
        return match 