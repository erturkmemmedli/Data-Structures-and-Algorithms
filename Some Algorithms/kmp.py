class Solution:
    def sTr(self, haystack, needle):
        string = needle + '-' + haystack
        lps = self.KMP_prefix(string)
        for i in range(len(needle)+1, len(string)):
            if lps[i] == len(needle):
                return i - 2 * len(needle)
        return -1
        
    def KMP_prefix(self, pattern):
        prefix = [0] * len(pattern)
        border = 0
        for i in range(1, len(pattern)):
            while border > 0 and pattern[i] != pattern[border]:
                border = prefix[border - 1]
            if pattern[i] == pattern[border]:
                border += 1
            else:
                border = 0
            prefix[i] = border
        return prefix
