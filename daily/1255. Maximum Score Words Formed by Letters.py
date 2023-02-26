"""
每日一题：2023.02.26
题目链接：https://leetcode.cn/problems/maximum-score-words-formed-by-letters/
标签：子集型回溯
思路：对于 words 逐个遍历，对于每一个 words[i] 考虑两种情况：选择或者不选；
通过外部变量 res 记录所有情况下能获得的最大分数。

在选择 words[i] 时，需要关注剩余的 letters 是否足够拼完整个单词；
根据回溯算法的需要，在选择 words[i] 之后，需要在返回之后将使用的字母复原。
"""

from string import ascii_lowercase
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = Counter(letters)
        letter_score = dict(zip(ascii_lowercase, score))
        res = 0
        n = len(words)

        def dfs(i, total):
            if i == n:
                nonlocal res
                res = max(res, total)
                return
            
            # 不选择 words[i]
            dfs(i+1, total)

            # 选择 words[i]
            # 关注剩余的 letters 是否足够拼完整个单词
            for j, c in enumerate(words[i]):
                if cnt[c] == 0:
                    for ch in words[i][:j]:
                        cnt[ch] += 1
                    return
                cnt[c] -= 1
                total += letter_score[c]
            
            dfs(i+1, total)

            # 在返回之后将 words[i] 使用的字母复原
            for c in words[i]:
                cnt[c] += 1
        
        dfs(0, 0)
        return res
