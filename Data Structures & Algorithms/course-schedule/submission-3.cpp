class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);

        for (auto& p : prerequisites) {
            adj[p[1]].push_back(p[0]);
        }

        vector<int> state(numCourses, 0); // 0 = unvisited, 1 = visited in path, 2 = done
        for (int i = 0; i < numCourses; ++i) {
            if (hasCycle(adj, state, i)) return false;
        }

        return true;
    }

private:
    bool hasCycle(vector<vector<int>>& adj, vector<int>& state, int i) {
        if (state[i] == 1) return true;
        if (state[i] == 2) return false;

        state[i] = 1;
        for (int v : adj[i]) {
            if (hasCycle(adj, state, v)) return true;
        }
        state[i] = 2;

        return false;
    }
};
