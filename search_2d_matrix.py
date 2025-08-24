from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = self.binary_search(matrix, target)
        return result != -1

    def binary_search(self, matrix, target, left=0, right=None):
        if right is None:
            right = len(matrix) -1
        
        if left > right:
            return -1
        
        mid = (left+right)//2
        if target in matrix[mid]:
            return True
        elif target > matrix[mid][-1]:
            return self.binary_search(matrix, target, mid+1, right)
        elif target < matrix[mid][0]:
            return self.binary_search(matrix, target, left, mid-1)
        else:
            return -1

