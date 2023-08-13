class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {

        vector<vector<int>> ans;
        vector<int>curr = {};

        backtrack(curr, nums, ans);
        return ans;
        
    }

    void backtrack(vector<int>&curr, vector<int>&nums,vector<vector<int>>&ans)
    {
        if(curr.size() == nums.size())
        {
            for(auto x: curr)
            {
                cout<<x<<'\t';
            }
            cout<<"End of a batch \n";
            ans.push_back(curr);
            return;
        }

        for(int num: nums)
        {
            if(find(curr.begin(), curr.end(), num) == curr.end())
            {
                curr.push_back(num);
                backtrack(curr, nums, ans);
                curr.pop_back();
            }
        }

    }


};
