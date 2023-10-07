class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while 1:
            if num == 0:
                break
            if num % 2 == 0:
                num = num / 2
                step += 1
            if num % 2 == 1:
                num -= 1
                step += 1
        return(step)