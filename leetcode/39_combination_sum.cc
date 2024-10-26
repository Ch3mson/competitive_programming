class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>result;
        vector<int>currCandidates;
        dfs(0, target, candidates, currCandidates, result);
        return result;
    }

private:
    void dfs(int i, int target, vector<int>& candidates, vector<int>& currCandidates, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(currCandidates);
            return;
        }
        if (target < 0 || i >= candidates.size()) {
            return;
        }
        currCandidates.push_back(candidates[i]);
        dfs(i, target - candidates[i], candidates, currCandidates, result);
        currCandidates.pop_back();
        dfs(i+1, target, candidates, currCandidates, result);
    }
};
