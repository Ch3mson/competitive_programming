class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        // hash map that keeps track of all numbers occurances
        // Traverse through map, going from smallest to largets numbers

        int n = nums.size();
        map<int, int> occurrences; // num: occurrences

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums[i].size(); j++) {
                occurrences[nums[i][j]]++;
            }
        }

        // traverse through occurances map, checking if it's = to n occurrences
        vector<int> output;
        for (const auto occ : occurrences) {
            if (occ.second == n) {
                output.push_back(occ.first);
            }
        }
        return output;
    }
};
