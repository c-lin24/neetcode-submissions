class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dfs(i) means the suffix can be split starting from i: s[i:]
        memo = {len(s) : True} #empty string

        def dfs(i):
            if i in memo: 
                return memo[i]

            for w in wordDict: 
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)