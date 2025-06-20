public class Solution {
    public static int getMoneySpent(int[] keyboards, int[] drives, int b) {
        int max = -1;
        for (int k : keyboards) {
            for (int d : drives) {
                if (k + d <= b) max = Math.max(max, k + d);
            }
        }
        return max;
    }
}