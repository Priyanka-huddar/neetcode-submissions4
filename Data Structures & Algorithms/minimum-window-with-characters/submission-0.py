from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        windows = {}
        have = 0
        need_count = len(need)
        left = 0
        res_len = float("inf")
        res_left = 0

        for right in range(len(s)):
            ch = s[right]
            windows[ch] = windows.get(ch, 0) + 1

            if ch in need and windows[ch] == need[ch]:
                have += 1

            # Safe shrink: also ensure left <= right
            while have == need_count and left <= right:
                curr_len = right - left + 1
                if curr_len < res_len:
                    res_len = curr_len
                    res_left = left

                left_ch = s[left]
                windows[left_ch] = windows.get(left_ch, 0) - 1

                if left_ch in need and windows[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if res_len == float('inf'):
            return ""
        return s[res_left:res_left + res_len]