/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */

// @lc code=start
#include <stdio.h>      /* printf */
#include <stdlib.h>  
class Solution {
public:
    double myPow(double x, int n) {
        double result = 1;
        if(n == 0) {
            return 1;
        }
        if(x == 1.0) {
            return 1.0;
        }
        if(x == -1.0) {
            if(n&2 == 0) {
                return 1;
            }
            return -1;
        }
        for(int i=0; i<abs(n); i++) {
            result *= x;
        }
        if(n > 0) {
            return result;
        }
        return 1/result;
    }
};
// @lc code=end

