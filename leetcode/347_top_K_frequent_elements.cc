class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);
        for (const auto& pair : counts) {
            int number = pair.first;
            int amount = pair.second;
            buckets[amount].push_back(number);
        }

        vector<int> result;
        for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) break;
            }
        }
        return result;
    }
};
