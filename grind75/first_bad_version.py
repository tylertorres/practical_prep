# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            version = (left + right) // 2

            if not isBadVersion(version):
                left = version + 1
            else:
                right = version

        return left
