/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        dfs(root, 0);
        return v_;
    }

private: 
    void dfs(TreeNode* root, size_t depth) {
        if (!root) return;
        if (depth == v_.size()) v_.push_back(root->val); 
        dfs(root->right, depth+1);
        dfs(root->left, depth+1);
    }
    vector<int> v_;
};
