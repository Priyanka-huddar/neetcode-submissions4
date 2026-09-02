class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have, need_unique = 0, len(need)
        left, best = 0, (float("inf"), 0)  # (length, start)

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1  # this line was missing

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_unique:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left)

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        if best[0] == float("inf"):
            return ""
        return s[best[1]:best[1] + best[0]]