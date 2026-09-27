class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> mins;
        vector<int> maxs;
        mins.push_back(nums[0]);
        maxs.push_back(nums[0]);

        // mins and maxs[i] is the min and max product subarray until i

        for (int i = 1; i < nums.size(); ++i) {
            auto [lo, hi] = minmax({
                mins[i-1] * nums[i],
                maxs[i-1] * nums[i],
                nums[i]
            });
            mins.push_back(lo);
            maxs.push_back(hi);
        }

        return *max_element(maxs.begin(), maxs.end());
    }
};
