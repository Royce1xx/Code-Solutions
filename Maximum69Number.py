class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        royce = []
        count = 0
        
        for i in range(len(num)):
            if count == 1:
                royce.append(num[i])
            elif num[i] == "9":
                royce.append(num[i])
            
            elif num[i] == "6":
                royce.append("9")
                count += 1

                
        
        return int("".join(royce))
