class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int maxRows = grid.size();
        int maxCols = grid[0].size();
        for (int r = 0; r < maxRows; r++) {
            for (int c = 0; c < maxCols; c++) {
                if (grid[r][c] == 1) {
                    maxArea = max(maxArea, bfs(r, c, grid));
                }
            }
        }
        return maxArea;
    }
private:
    int bfs(int r, int c, vector<vector<int>>& grid) {
        int area = 0;
        int maxRows = grid.size();
        int maxCols = grid[0].size();
        queue<pair<int,int>>q;
        vector<pair<int,int>>directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        q.push({r,c});
        grid[r][c] = 0;
        area++;
        while (!q.empty()) {
            auto [currRow, currCol] = q.front();
            q.pop();
            grid[currRow][currCol] = 0;
            for (auto dir : directions) {
                int newRow = currRow + dir.first;
                int newCol = currCol + dir.second;
                if (newRow >= 0 && newCol >= 0 && newRow < maxRows && newCol < maxCols && grid[newRow][newCol] == 1) {
                    grid[newRow][newCol] = 0;
                    q.push({newRow, newCol});
                    area++;
                }
            }
        }
        return area;
    }
};
