from typing import List


def search(nums: List[int], target: int) -> int:

    low = 0
    hight = len(nums) - 1

    while low <= hight:
        mid = (low + hight) // 2
        if nums[mid] > target:
            hight = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


search([x for x in range(100)], 12)
