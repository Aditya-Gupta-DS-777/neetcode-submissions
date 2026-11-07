
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

            maxf = max(maxf, mp[r])  

            winlen = i - l + 1
            ka = winlen - maxf

            
            if ka > k:
                mp[s[l]] -= 1  
                l += 1         

            winlen = i - l + 1  
            res = max(res, winlen)  

        return res
