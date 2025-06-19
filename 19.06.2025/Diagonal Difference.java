import java.util.*;
public class Solution {
    public static int diagonalDifference(List<List<Integer>> arr) {
        int n = arr.size(), leftSum = 0, rightSum = 0;
        for (int i = 0; i < n; i++) {
            leftSum += arr.get(i).get(i);
            rightSum += arr.get(i).get(n - 1 - i);
        }
        return Math.abs(leftSum - rightSum);
    }
}