class Solution(object):
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    def kidsWithCandies(candies, extraCandies):
        max_candies = max(candies)

        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
    print(kidsWithCandies(candies, extraCandies))


"""
def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append('true')
            else:
                result.append('false')
        return result
"""

