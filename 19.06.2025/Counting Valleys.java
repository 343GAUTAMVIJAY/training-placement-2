public class Solution {
    public static int countingValleys(int steps, String path) {
        int altitude = 0, valleys = 0;
        for (char step : path.toCharArray()) {
            if (step == 'U') altitude++;
            else {
                if (altitude == 0) valleys++;
                altitude--;
            }
        }
        return valleys;
    }
}