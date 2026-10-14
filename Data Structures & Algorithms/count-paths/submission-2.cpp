class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n*m);

        for (size_t i = 0; i < m; ++i) dp[i*n + n-1] = 1;
        for (size_t i = 0; i < n; ++i) dp[(m-1)*n + i] = 1;

        for (int i = m - 2; i >= 0; --i) {
            for (int j = n - 2; j >= 0; --j) {
                dp[i * n + j] = dp[i*n + j + 1] + dp[(i+1)*n + j]; 
            }
        }

        return dp[0];
    }
};
