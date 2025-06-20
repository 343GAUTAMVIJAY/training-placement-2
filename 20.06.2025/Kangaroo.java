public class Solution {
    public static String kangaroo(int x1, int v1, int x2, int v2) {
        if (v1 <= v2) return "NO";
        int diff = x2 - x1, speedDiff = v1 - v2;
        return diff % speedDiff == 0 && diff / speedDiff >= 0 ? "YES" : "NO";
    }
}