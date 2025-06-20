public class Solution {
    public static String catAndMouse(int x, int y, int z) {
        int distA = Math.abs(x - z), distB = Math.abs(y - z);
        return distA < distB ? "Cat A" : distB < distA ? "Cat B" : "Mouse C";
    }
}