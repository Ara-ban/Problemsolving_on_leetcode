#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class MinStack {
public:
    std::stack<int> stk;
    std::stack<int> minStack;
    
    MinStack() {
    }
    
    void push(int val) {
        stk.push(val);
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        }
    }
    
    void pop() {
        if (stk.top() == minStack.top()) {
            minStack.pop();
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};