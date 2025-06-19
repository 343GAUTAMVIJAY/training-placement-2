import java.util.*;
public class Solution {
    public static void miniMaxSum(List<Integer> arr) {
        Collections.sort(arr);
        long minSum = 0, maxSum = 0;
        for (int i = 0; i < 4; i++) minSum += arr.get(i);
        for (int i = 1; i < 5; i++) maxSum += arr.get(i);
        System.out.println(minSum + " " + maxSum);
    }
}