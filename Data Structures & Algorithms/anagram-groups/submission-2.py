from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # keys: list of alphabets

        for word in strs:
            cur = [0] * 26 #list of alphabets, indexed by alphabets
            for char in word:
                cur[ord(char) - ord('a')] += 1
            
            d[tuple(cur)].append(word)
        
        return list(d.values())
                
            