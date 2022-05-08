#include<iostream>
using namespace std;

class Solution
{
    public:
        Solution();
        int lengthOfLongestSubstring(string s) {
        
        }
};

int main(int argc, char const *argv[])
{
    Solution *solver = new Solution();
    int result = solver->lengthOfLongestSubstring("abcabcbb");
    cout << result << endl;
    return 0;
}