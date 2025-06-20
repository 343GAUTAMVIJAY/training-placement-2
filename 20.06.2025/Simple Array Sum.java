import java.util.*;
public class Solution {
    public static int simpleArraySum(List<Integer> ar) {
        int sum = 0;
        for (int num : ar) sum += num;
        return sum;
    }
}