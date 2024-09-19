#include <string>
#include <vector>
#include <stack>
using namespace std;
struct State
{
    string current;
    int open;
    int close;
};
class Solution
{
public:
    vector<string> generateParenthesis(int n)
    {
        vector<string> result;
        if (n == 0)
            return result;

        stack<State> stk;
        stk.push(State{"", 0, 0});
        while (!stk.empty())
        {
            State top = stk.top();
            stk.pop();
            if (top.current.length() == 2 * n)
            {
                result.push_back(top.current);
                continue;
            }
            if (top.open < n)
            {
                State newState = top;
                newState.current += '(';
                newState.open += 1;
                stk.push(newState);
            }
            if (top.close < top.open)
            {
                State newState = top;
                newState.current += ')';
                newState.close += 1;
                stk.push(newState);
            }
        }
        return result;
    }
};