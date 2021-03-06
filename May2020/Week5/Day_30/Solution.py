class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        
Time Complexity : O(NlogN)

Space Complexity: O(N). This space for sorting given list.


