class Solution:
    J = input("Give distinct characters of jewels: ")
    S = input("Give all characters of stones you have: ")
    counterJewels = 0
    def numJewelsInStones(self):
        for i in range(len(self.S)):
            for j in range(len(self.J)):
                if self.S[i] == self.J[j]:
                    self.counterJewels += 1
        return self.counterJewels


##     ##     ##     ##     ##     ##     ##     ##     ##     ##     
myKollection = Solution()
print(myKollection.numJewelsInStones())
