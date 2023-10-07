class Solution(object):
    def numberOfSteps(self, num):
        k=0
        while num!=0:
            if num%2==0:
                num=num/2                
            else:
                num-=1
            k+=1
        return k