#include <map>
#include <iostream>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mapping;
        int i = 0;
        for(i=0; i< strs.size(); i++){
            string sorted_string = strs[i];
            sort(sorted_string.begin(), sorted_string.end());
            
            if(mapping.find(sorted_string) != mapping.end()){
                mapping[sorted_string].push_back(strs[i]);
            }
            else{
                mapping.insert({sorted_string, {strs[i]}});
            }
        }
        
        vector<vector<string>> res;
        for(map<string, vector<string>>::iterator it = mapping.begin(); it != mapping.end(); ++it) {
          res.push_back(it->second);
          //cout << it->second << "\n";
        }
        
        return res;
    }
};