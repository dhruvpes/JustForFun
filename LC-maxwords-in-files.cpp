class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {

        int res = INT_MIN;
        for(int i = 0; i < sentences.size(); ++i)
        {
            int temp = 0;
            for(int j = 0; j<sentences[i].size(); j++)
            {
                if(sentences[i][j] == ' ') ++temp;
            }

            res = max(res, temp);
        }

    return res+1;
    }
};
