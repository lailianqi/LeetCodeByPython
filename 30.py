from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        滑动窗口的写法  有点牛逼
        https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation
        """
        result = []
        if not words or len(s) < len(words[0])*len(words):
            return result
        wl, count, n, word_dict = len(words[0]), len(words), len(s), {}
        word_dict = Counter(words)
        for i in range(wl):
            left, cnt, tmp_dict = i, 0, {}
            for j in range(i, n-wl+1, wl):
                strs = s[j:j+wl]
                if strs in word_dict:
                    cnt += 1
                    tmp_dict[strs] = tmp_dict.get(strs, 0) + 1
                    while tmp_dict[strs] > word_dict[strs]:
                        tmp_dict[s[left: left+wl]] -= 1
                        left += wl
                        cnt -= 1
                    if cnt == count:
                        result.append(left)
                        tmp_dict[s[left: left+wl]] -= 1
                        left += wl
                        cnt -= 1
                else:
                    left, cnt, tmp_dict = j+wl, 0, {}
        return result
