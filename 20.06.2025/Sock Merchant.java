import java.util.*;
public class Solution {
    public static int sockMerchant(int n, List<Integer> ar) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int sock : ar) count.put(sock, count.getOrDefault(sock, 0) + 1);
        int pairs = 0;
        for (int freq : count.values()) pairs += freq / 2;
        return pairs;
    }
}