class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        alpha = {}
        max_count = 0

        for r in range(len(s)):
            alpha[s[r]] = 1 + alpha.get(s[r], 0)
            max_count = max(max_count, alpha[s[r]])

            while (r - l + 1) - max_count > k:
                alpha[s[l]] -= 1
                l += 1

        res = max(res, r - l + 1)
        return res