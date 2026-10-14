class Solution {
    vector<int> a;
    vector<vector<int>> memo;

    int solve(int l, int r) { // max coins in [l, r], assuming a[l-1] and a[r+1] stay alive
        if (l > r) return 0;

        int& best = memo[l][r];
        if (best != -1) return best;   // already computed

        best = 0;
        for (int i = l; i <= r; ++i) {
            int coins = a[l-1] * a[i] * a[r+1];
            best = max(best, coins + solve(l, i-1) + solve(i+1, r));
        }
        return best;
    }

public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        a = {1};
        a.insert(a.end(), nums.begin(), nums.end());
        a.push_back(1);

        memo.assign(n + 2, vector<int>(n + 2, -1));
        return solve(1, n);
    }
};