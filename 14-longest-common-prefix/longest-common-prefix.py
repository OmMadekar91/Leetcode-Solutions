class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        for i in strs:
            if len(i) < len(prefix) or prefix == '':
                prefix = i
        while True:
            count = 0
            for i in strs:
                if prefix == i[:len(prefix)]:
                    count += 1
            if count == len(strs):
                return prefix
            prefix = prefix[:-1]
            if prefix == '':
                return ''