#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;
        std::unordered_map<char,char> bracket_pairs = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        for (char c : s){
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            }
            else {
                if (stk.empty() || stk.top() != bracket_pairs[c]){
                    return false ; 
                }
                else {
                    stk.pop();
                }
            }
        }
        return stk.empty();
    }
};