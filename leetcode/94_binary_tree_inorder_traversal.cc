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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>output;
        inorder(root, output);
        return output;
    }

private:
    void inorder(TreeNode* ptr, vector<int>& response) {
        if (!ptr) {
            return;
        }
        inorder(ptr->left, response);
        response.push_back(ptr->val);
        inorder(ptr->right, response);
    }
};
