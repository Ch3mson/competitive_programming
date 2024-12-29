class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 1; i++) {
            int l =  i + 1;
            int r = nums.size() - 1;
            if (nums[i] > 0) break;
            // skip over duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            while (l < r) {
                if (nums[l] + nums[r] + nums[i] == 0) {
                    output.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                } else if (nums[l] + nums[r] + nums[i] < 0) {
                    l++;
                } else if (nums[l] + nums[r] + nums[i] > 0) {
                    r--;
                }
            }
        }

        return output;
    }
};
