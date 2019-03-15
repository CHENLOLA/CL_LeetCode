'''
Design and implement a TwoSum class. It should support the following operations:add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

'''
class TwoSum:
    def __init__(self):
        self.num_hash={}

    def add(self,num):
        if num in self.num_hash:
            self.num_hash+=1
        else
            self.num_hash[num]=1
    def find(self,n):
        num_hash=self.num_hash
        for i in num_hash:
            sub=n-i
            if sub in num_hash and (sub!=i or num_hash[sub]>1):
                return True
            else: return False

