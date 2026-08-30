class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if t_sorted == s_sorted:
            return True
        else:
            return False

        # for s in s_sorted:
        #     for t in t_sorted:
        #         if (s not in t_sorted):
        #             print(t_sorted)
        #             return False
        #         else:
        #             return True
    