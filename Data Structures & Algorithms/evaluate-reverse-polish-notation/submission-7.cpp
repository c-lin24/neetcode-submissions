class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        stack<int> nums;
        unordered_set<string> ops{"+", "-", "*", "/"};

        for (int i = 0; i < tokens.size(); ++i) {
            if (ops.contains(tokens[i])) {
                int n1 = nums.top();
                nums.pop();
                int n2 = nums.top();
                nums.pop();

                int s;
                switch (tokens[i][0]) {
                    case '+':
                        s = n1 + n2;
                        break;
                    case '-':
                        s = n2 - n1;
                        break;
                    case '*':
                        s = n1 * n2;
                        break;
                    case '/':
                        s = n2 / n1;
                        break;
                }
                nums.push(s);
            } else {
                nums.push(stoi(tokens[i]));
            }
        }

        return nums.top();

    }
};
