#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>mapping;
        vector<int> res;
        int i = 0;
        for(i=0; i < nums.size(); i++){
            if(mapping.find(target - nums[i]) != mapping.end()){
                res.push_back(mapping[target - nums[i]]);
                res.push_back(i);
                return res;
            }
            else{
                mapping[nums[i]] = i;
            }
        }
        return {};
    }
};