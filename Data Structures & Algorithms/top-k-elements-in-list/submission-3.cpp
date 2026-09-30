class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;

        for (int n : nums) ++m[n];
        
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [v, c] : m) buckets[c].push_back(v);

        vector<int> res;
        for (int c = nums.size(); c > 0 && (int)res.size() < k; --c)
            for (int v : buckets[c]) {
                res.push_back(v);
                if ((int)res.size() == k) break;
            }
        return res;

    }
};
