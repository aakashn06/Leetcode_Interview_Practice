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
        while leftIdx != rightIdx:
            area = computeArea(leftIdx, rightIdx, height[leftIdx], height[rightIdx])
            if area > maxArea:
                maxArea = area
            if height[leftIdx] > height[rightIdx] or height[leftIdx + 1] > height[rightIdx - 1]:
                prevHeight = height[rightIdx]
                rightIdx -= 1
                while height[rightIdx] <= prevHeight and rightIdx > leftIdx:
                    rightIdx -= 1
            elif if height[leftIdx] < height[rightIdx] or height[leftIdx + 1] < height[rightIdx - 1]:
                prevHeight = height[leftIdx]
                leftIdx += 1
                while height[leftIdx] <= prevHeight and rightIdx > leftIdx:
                    leftIdx += 1
            else:
                leftIdx2 = leftIdx + 1
                rightIdx2 = rightIdx - 1
                while leftIdx2 == rightIdx2:
                    area = computeArea(leftIdx2, rightIdx, heights[leftIdx2], heights[rightIdx])
                    if area > maxArea:
                        maxArea = area
                    leftIdx2 = leftIdx + 1
                    rightIdx2 = rightIdx - 1
                

        """
        :type height: List[int]
        :rtype: int
        """
        
