class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0;
        int boundary = mat.size();

        for (int r = 0; r < boundary; r++) {
            if (r == boundary - r - 1) {
                sum += mat[r][r];
            } else {
                sum += mat[r][r];
                sum += mat[r][boundary - r - 1];
            }
        }

        return sum;
    }
};



// 0,0 1,1 2,2 3,3
// 0,3 1,2 2,1 3,0
