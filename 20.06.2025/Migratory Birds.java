import java.util.*;
public class Solution {
    public static int migratoryBirds(List<Integer> arr) {
        int[] count = new int[6];
        for (int bird : arr) count[bird]++;
        int maxCount = 0, result = 0;
        for (int i = 1; i <= 5; i++) {
            if (count[i] > maxCount) {
                maxCount = count[i];
                result = i;
            }
        }
        return result;
    }
}