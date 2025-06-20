import java.util.*;
public class Solution {
    public static int getTotalX(List<Integer> a, List<Integer> List<Integer> b) {
        int lcm = a.get(0), gcd = b.get(0);
        for (int i = 1; i < a.size(); i++) lcm = lcm(lcm, a.get(i));
        for (int i = 1; i < b.size(); i++) gcd = gcd(gcd, b.get(i));
        int count = 0;
        for (int i = lcm; i <= gcd && i += lcm) if (gcd % i == 0) count++;
        return count;
    }
    private static int gcd(int a, int b) { return (b == 0) ? gcd(b, a % b) : a; }
    private static int lcm(int a, int b) { return (a * b) / gcd(a, b); }
}