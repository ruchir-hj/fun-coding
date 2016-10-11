class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> res;
        if(nums1.empty()||nums2.empty()) return res;
        auto comp = [nums1,nums2](pair<int, int>&a, pair<int, int>&b) {
        return nums1[a.first] + nums2[a.second] > nums1[b.first] + nums2[b.second];
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> q(comp);
    for (int i = 0;i < nums1.size() && i < k;i++) {
        q.push({ i, 0 });
    }
    for (int i = 0;i < k&&(!q.empty());i++) {
        pair<int, int> temp = q.top();
        q.pop();
        res.push_back({nums1[temp.first], nums2[temp.second]});
        if (temp.second < nums2.size() - 1) q.push({ temp.first,temp.second + 1 });
    }
    return res;
    }
};