def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    max_length = 0
    look_up = {}
    for end, alpha in enumerate(s):
        if alpha in look_up:
            start = max(start, look_up[alpha] + 1)
        look_up[alpha] = end
        max_length = max(max_length, end - start + 1)
    return max_length
