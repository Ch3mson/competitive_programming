class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        int boundary = matrix.size();
        
        unordered_set<int> cols, rows;

        for (int r = 0; r < boundary; r++) {
            for (int c = 0; c < boundary; c++) {
                if (rows.find(matrix[r][c]) != rows.end()) {
                    return false;
                } else {
                    rows.insert(matrix[r][c]);
                }

                if (cols.find(matrix[c][r]) != cols.end()) {
                    return false;
                } else {
                    cols.insert(matrix[c][r]);
                }
            }

            cols.clear();
            rows.clear();
        }

        return true;

    }
};
