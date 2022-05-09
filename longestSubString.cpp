// problem 3
#include<iostream>
#include<set>
using namespace std;

class Solution
{
    public:
        Solution(){}
        int lengthOfLongestSubstring(string s) 
		{	
			set<char> window = {};
			int left_index = 0;
			int longest_len = 0;

			for (int r_index = 0; r_index < s.length(); r_index++)
			{
				while (window.find(s[r_index]) != window.end())
				{
					window.erase(s[left_index]);
					left_index++;
				}
				window.insert(s[r_index]);
				longest_len = (longest_len > window.size()) ? longest_len : window.size();
			}
			return longest_len;
        }
};

int main(int argc, char const *argv[])
{
    Solution *solver = new Solution();
    int result = solver->lengthOfLongestSubstring("abcabcbb");
    cout << result << endl;
    return 0;
}
