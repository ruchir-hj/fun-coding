// O(1) space

class Solution {
public:

    int digitSquareSum(int n) {
        int sum = 0, tmp;
        while (n != 0) {
            tmp = n % 10;
            sum += tmp * tmp;
            n /= 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow = n, fast = digitSquareSum(n);

        while (slow != fast) {
            slow = digitSquareSum(slow);
            fast = digitSquareSum(digitSquareSum(fast));
        }

        return slow == 1;

    }

};