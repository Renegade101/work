class Solution(object):
    def romanToInt(self, s):
        ltr =  {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

        num = 0

        for i in range(len(s) - 1):
            if ltr[s[i]] < ltr[s[i + 1]]:
                num -= ltr[s[i]]
            else:
                num += ltr[s[i]]
        return num + ltr[s[-1]]

        """
        :type s: str
        :rtype: int
        """