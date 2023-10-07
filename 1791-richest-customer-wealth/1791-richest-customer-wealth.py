class Solution(object):
    def maximumWealth(self, accounts):
        maxi=0;
        maxfinal=0;
        for i in range(0, len(accounts)):
            maxi=0;
            for j in range(0, len(accounts[i])):
                maxi += accounts[i][j]
            if maxfinal<maxi:
                maxfinal=maxi
                
                    
        return maxfinal

        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        