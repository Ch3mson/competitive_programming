class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> output;

        for (int i : nums2) {
            if (set1.count(i)) {
                output.insert(i);
            }
        }

        return vector(output.begin(), output.end());
    }
};
