
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];

            if (mp.find(need) != mp.end()) {
                return {mp[need], i};
            }

            mp[nums[i]] = i;
        }

        return {};
    }
};

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    Solution s;
    vector<int> ans = s.twoSum(nums, target);

    cout << ans[0] << " " << ans[1] << endl;
    return 0;
}
