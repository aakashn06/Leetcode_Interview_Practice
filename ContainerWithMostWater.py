class Solution(object):
    def maxArea(self, height):
        def computeArea(index1, index2, height1, height2):
            if height1 >= height2:
                height = height2
            else:
                height = height1
            width = abs(height2 - height1)
            return (width * height)
        
        leftIdx = 0
        rightIdx = len(height) - 1
        maxArea = 0
        while (rightIdx - leftIdx) > 0:
            area = computeArea(leftIdx, rightIdx, height[leftIdx], height[rightIdx])
            if area > maxArea:
                maxArea = area
            if height[leftIdx] > height[rightIdx]:
                prevHeight = height[rightIdx]
                rightIdx -= 1
                while height[rightIdx] <= prevHeight and rightIdx > leftIdx:
                    rightIdx -= 1
            elif height[leftIdx] < height[rightIdx]:
                prevHeight = height[leftIdx]
                leftIdx += 1
                while height[leftIdx] <= prevHeight and rightIdx > leftIdx:
                    leftIdx += 1
            else:
                leftIdx2 = leftIdx + 1
                rightIdx2 = rightIdx - 1
                while height[leftIdx2] == height[rightIdx2] and (rightIdx2 - leftIdx2) > 0:
                    area = computeArea(leftIdx2, rightIdx, height[leftIdx2], height[rightIdx])
                    if area > maxArea:
                        maxArea = area
                    leftIdx2 = leftIdx + 1
                    rightIdx2 = rightIdx - 1
            return maxArea
                

        """
        :type height: List[int]
        :rtype: int
        """
        
