struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        vector<int> res = robHelper(root);
        return max(res[0], res[1]);
    }

private:
    vector<int> robHelper(TreeNode* root) {
        if (root == NULL) {
            return vector<int>(2,0);
        }

        vector<int> left = robHelper(root->left);
        vector<int> right = robHelper(root->right);

        vector<int> res(2,0);
        res[0] = max(left[0], left[1]) + max(right[0], right[1]);
        res[1] = root->val + left[0] + right[0];

        return res;
    }
};