import java.util.*;
public class Solution {
    public static int lonelyinteger(List<Integer> a) {
        int result = 0;
        for (int num : a) result ^= num;
        return result;
    }
}