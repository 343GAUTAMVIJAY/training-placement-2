public class Solution {
    public static int pageCount(int n, int p) {
        int fromStart = p / 2;
        int fromEnd = (n % 2 == 0 ? (n + 1 - p) / 2 : (n - p) / 2);
        return Math.min(fromStart, fromEnd);
    }
}