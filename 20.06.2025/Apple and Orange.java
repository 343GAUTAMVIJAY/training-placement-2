public class Solution {
    public static void countApplesAndOranges(int s, int t, int a, int b, List<Integer> apples, List<Integer> oranges) {
        int appleCount = 0, orangeCount = 0;
        for (int apple : apples) if (a + apple >= s && a + apple <= t) appleCount++;
        for (int orange : oranges) if (b + orange >= s && b + orange <= t) orangeCount++;
        System.out.println(appleCount);
        System.out.println(orangeCount);
    }
}