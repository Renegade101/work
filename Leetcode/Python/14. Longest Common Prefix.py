class Solution(object):
    strs = ["flower", "flow", "flight"]
    def longestCommonPrefix(strs):
        if len(strs) == 0:
            return ''

        base = strs[0]
        for n in range(len(base)):
            for word in strs[1:]:
                if (n == len(word) or word[n] != base[n]):
                    return base[0:n]
        return base
    print(longestCommonPrefix(strs))


