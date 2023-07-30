//1710 -  Maximum Units on a Truck


class Solution {
public:
    static bool myFunc(vector<int>&a, vector<int>&b)
    {
        return a[1] > b[1];
    }


    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) 
    {
        sort(boxTypes.begin(), boxTypes.end(), myFunc);
        
        int res = 0;

        for(auto box: boxTypes)
        {
            int x = min(box[0], truckSize);
            res = res + (x*box[1]);
            truckSize = truckSize - x;
            if(truckSize == 0) break;

        }

    return res;
        
    }
};