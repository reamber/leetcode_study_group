class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        curr_profit = 0 #var to track the new profit getting calculated
        max_profit = 0 #the answer we want to return
        min_buytime = prices[0] #the minimum buy price initialized to prices[0]
        
        #to maximize profit, we want high sell price and min buy price
        
        for i in range(len(prices)):
            min_buytime = min(min_buytime, prices[i]) #compare and take the min buy price
            curr_profit = prices[i] - min_buytime #profit = sell - buy
            if (curr_profit > max_profit):
                max_profit = curr_profit
                
        return max_profit
            
            
    
        
