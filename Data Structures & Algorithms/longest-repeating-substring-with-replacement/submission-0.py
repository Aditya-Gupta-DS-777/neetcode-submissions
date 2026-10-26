
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mp = {}
        l = 0
        maxf = 0  # NEW: window mein maximum frequency track karne ke liye

        for i, r in enumerate(s):
            if r in mp:
                mp[r] += 1
            else:
                mp[r] = 1

            maxf = max(maxf, mp[r])  # NEW: maximum frequency update karo

            winlen = i - l + 1
            ka = winlen - maxf

            # NEW: invalid window hone par left pointer move karo
            if ka > k:
                mp[s[l]] -= 1  # NEW: left character ki frequency kam karo
                l += 1         # NEW: left pointer ko aage badhao

            winlen = i - l + 1  # NEW: updated window length calculate karo
            res = max(res, winlen)  # CHANGE: maximum result save karo

        return res
