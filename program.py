class Solution:
    J = input("Give distinct characters of jewels: ")
    S = input("Give all characters of stones you have: ")
    counter = 0
    def numJewelsInStones(self):
        for i in range(len(self.S)):
            for j in range(len(self.J)):
                if self.S[i] == self.J[j]:
                    self.counter += 1
        print(self.counter)


##     ##     ##     ##     ##     ##     ##     ##     ##     ##     
myKollection = Solution()
print(myKollection.numJewelsInStones())
