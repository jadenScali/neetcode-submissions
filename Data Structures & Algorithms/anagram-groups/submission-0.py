def hash_value(s) -> int:
    return tuple(sorted(s))

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_value_map = {}
        anagram_groups = []

        num_groups = 0


        for s in strs:
            letters_value = hash_value(s)
    
            if letters_value not in anagram_value_map:
                anagram_value_map[letters_value] = num_groups
                anagram_groups.append([s])
                num_groups += 1
            else:
                anagram_groups[anagram_value_map[letters_value]].append(s)
        
        return anagram_groups
        