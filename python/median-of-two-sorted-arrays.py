# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:31:48 2020

@author: shrey
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        Brute force solution: O(m+n): merge the two arrays and get the median 
        
        This solution: O(log(min(m, n)))
        
        Here, binary search is applied over the smaller array to find a partition that satisfies the following condition:
        the max element of the left partition of the first array should be smaller than the min element of the right partition of the second array, similarly the max element of the left partition of the second array should be smaller than the right partition of the first array. 
        
        By this step, we get two partitions where all the elements of the first partition is lesser than the elements of the second partition, AND the two partitions have equal number of elements (left partition has 1 more if there are odd number of elements)
        
        When this is satisfied, the median is calculated using the following condition: 
        if the length of the two arrays add up to a odd number, median is the average of the max element of the left partition and min element of the right partition
        else, the median is the max of the left partition
        
        partitionX = (start + end)//2
        partitionY = (x + y + 1)//2 - partitionX
        The partition is calibrated according to this condition: 
        
        if max_left_X is bigger than min_right_Y, then end = partitionX -1 
        else: 
        start = partitionX + 1
        
        references: https://www.youtube.com/watch?time_continue=16&v=LPFhl65R7ww&feature=emb_logo
        """
        
        if len(nums1) > len(nums2):
            return Solution.findMedianSortedArrays(self, nums2, nums1)
        
        x = len(nums1)
        y = len(nums2)
        
        start = 0
        end = x
        
        while start <= end:
            partition_nums1 = (start + end)//2
            partition_nums2 = (x + y + 1)//2 - partition_nums1 
            
            # handling the case where the partition creates an empty list
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == x else nums1[partition_nums1]
            
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == y else nums2[partition_nums2]
            
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                
                if (x + y)%2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2))/2
                else:
                    return max(max_left_nums1, max_left_nums2)
            elif max_left_nums1 > min_right_nums2:
                end = partition_nums1 - 1
            else:
                start = partition_nums1 + 1
        
        # if you dont get any result, then the arrays must not be sorted
        print("Arrays not sorted")
        
        
            

                
            
            