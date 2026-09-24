class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string cur;
        vector<string> res;

        auto backtrack = [&](this auto &self, int open, int close) -> void {
            if (open == n && close == n) { res.push_back(cur); return;}
            if (open < n) {
                cur.push_back('(');
                self(open + 1, close);
                cur.pop_back();
            }
            if (close < open) {
                cur.push_back(')');
                self(open, close + 1);
                cur.pop_back();
            }
        };

        backtrack(0, 0);
        return res;
    }
};
