#include <unordered_set>
#include <algorithm>
#include <string>


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> st;
        int n = s.size();
        int l = 0;
        int maxl = 0;

        for (int r = 0; r < n; r++) {
            while (st.find(s[r]) != st.end(s[r])) {
                st.erase(s[l]);
                l++;
            }
            st.insert(s[r]);
            maxl = max(maxl, r - l + 1);
        }     

        return maxl;
    }  
};
