//486 - Predict the Winner


class Solution {
public:
    int optimize(vector<int>& nums, int i, int j, int chance)
    {
      if(i > j) return 0;
      
      if(chance == 0) return max(nums[i] + optimize(nums, i+1, j, 1), nums[j] +optimize(nums, i, j-1, 1));

      else return min(optimize(nums, i+1, j, 0) , optimize(nums, i, j-1, 0));


    }


    bool PredictTheWinner(vector<int>& nums) {

        bool res = true;

        int p1 = 0;
        int p2 = 0;

        int len = nums.size();

        for(int i = 0; i < len; ++i)
        {
            p2 = p2 + nums[i];
            
        }

        p1 = optimize(nums, 0, len -1, 0);
        p2 = p2 - p1;


        return (p1 >= p2);
    }
};