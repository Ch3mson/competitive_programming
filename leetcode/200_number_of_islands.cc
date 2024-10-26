class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rowSize = grid.size();
        int colSize = grid[0].size();
        int islands = 0;
        for (int r = 0; r < rowSize; r++) {
            for (int  c = 0; c < colSize; c++) {
                if (grid[r][c] == '1') {
                    bfs(r, c, grid);
                    islands++;
                }
            }
        }
        return islands;
    }
private:
    void bfs(int r, int c, vector<vector<char>>& grid) {
        int rowSize = grid.size();
        int colSize = grid[0].size();
        vector<pair<int,int>>directions = {{1, 0}, {-1 ,0}, {0, 1}, {0, -1}};
        queue<pair<int,int>>q;
        q.push({r, c});
        grid[r][c] = '0';
        while (!q.empty()) {
            auto [currRow, currCol] = q.front();
            q.pop();
            for (auto dir : directions) {
                int newRow = currRow + dir.first;
                int newCol = currCol + dir.second;
                if (newRow >= 0 && newCol >= 0 && newRow < rowSize && newCol < colSize && grid[newRow][newCol] =='1') {
                    grid[newRow][newCol] = '0';
                    q.push({newRow, newCol});
                }
            }
        }
    }
};
