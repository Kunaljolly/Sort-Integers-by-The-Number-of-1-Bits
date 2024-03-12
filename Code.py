class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_list=list(arr)
        sorted_list.sort(key= lambda x : (bin(x).count('1'),x))
        return sorted_list
        
        
