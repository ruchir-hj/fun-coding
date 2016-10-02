public class Solution {

    public boolean isHappy (int n) {
        Set<Integer> inLoop = new HashSet<Integer>();

        int squareSum, remain;
            while (inLoop.add(n)) {
                squareSum = 0;
                while (n >0) {
                    remain = n%10;
                    squareSum += remain * remain;
                    n /= 10;
                }
                if (squareSum == 1)
                    return true;
                else
                    n = squareSum;
            }
            return false;
    }
}




// O(1) space but TLE on time

/*
public class Solution {

    private int digitSquareSum (int n) {
        int sum = 0, temp;
         while (n != 0) {
            temp =  n %10;
            sum += (temp * temp);
            n /= 10;
         }
         return sum;
    }


    public boolean isHappy(int n) {
        int slow = n, fast = digitSquareSum(n);

        while (slow != fast) {
            slow = digitSquareSum(n);
            fast = digitSquareSum(digitSquareSum(n));

        }

        return slow == 1;

    }
}
*/