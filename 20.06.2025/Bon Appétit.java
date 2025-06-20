import java.util.*;
public class Solution {
    public static void bonAppetit(List<Integer> bill, int k, int b) {
        int total = 0;
        for (int i = 0; i < bill.size(); i++) if (i != k) total += bill.get(i);
        int fairShare = total / 2;
        System.out.println(b == fairShare ? "Bon Appetit" : b - fairShare);
    }
}