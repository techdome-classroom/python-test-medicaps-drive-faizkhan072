class Solution(object):
     def romanToInt(self, s:str):
        romanletter={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sumrez=0
        tempstr=list()
        for letter in s:
            for I,num1 in romanletter.items():
                if letter==I:
                    tempstr.append(int(num1))

        for i in range(len(tempstr)-1):
            if tempstr[i]<tempstr[i+1]:
                tempstr[i]=-tempstr[i]

        sumrez=sum(tempstr)
        return sumrez
        
        pass
