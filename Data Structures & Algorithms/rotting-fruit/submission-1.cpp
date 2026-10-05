class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int fresh = 0;

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) q.push(pair(i, j));
                else if (grid[i][j] == 1) fresh++; 
            }
        }

        int mins = 0;
        int dirs[] = {0, 1, 0, -1, 0};

        while (!q.empty() && fresh != 0) {
            for (int k = q.size(); k > 0; k--) {
                auto [r, c] = q.front();
                q.pop();
                for (int d = 0; d < 4; d++) {
                    int nr = r + dirs[d]; 
                    int nc = c + dirs[d+1];
                    if (nr < 0 || nc < 0 || nr >= grid.size() || nc >= grid[0].size() || grid[nr][nc] != 1) continue;
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push(pair(nr, nc));
                }
            }
            mins++;
        }
        return fresh ? -1 : mins;
    }
};
