from typing import List

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = [''.join(sorted(s)) for s in strs]
        anagrams_map = {}
        for i, s_sorted in enumerate(strs_sorted):
            if s_sorted in anagrams_map.keys():
                anagrams_map[s_sorted].append(strs[i])
            else:
                anagrams_map[s_sorted] = [strs[i]] 
        print(anagrams_map)
        return list(anagrams_map.values())      