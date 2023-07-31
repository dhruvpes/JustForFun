class Solution {
public:
    string sortSentence(string s) {

        string word;
        vector<string>v(20);
        
        for(int i = 0; i < s.size(); ++i)
        {
            if(s[i] >= 48 && s[i] <= 57)
            {
                v[s[i] - 48] = word + " ";
                word = "";
                i++;
                
            }
          
         else word += s[i];
        }

        string res = "";

        for(string x: v)
        {
            res += x;
        }

    res.pop_back();

    return res;
    }
};