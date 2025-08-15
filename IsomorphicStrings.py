class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        royce = {}
        doubleCheck = set()

        for letter, secondLetter in zip(s, t):
            if letter in royce:
                if royce[letter] != secondLetter:
                    return False
            
            else:
                if secondLetter in doubleCheck:
                    return False
                royce[letter] = secondLetter
                doubleCheck.add
        return True
        