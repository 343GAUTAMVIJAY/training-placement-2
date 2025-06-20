import java.util.*;
public class Solution {
    public static int birthdayCakeCandles(List<Integer> candles) {
        int max = Collections.max(candles), count = 0;
        for (int candle : candles) if (candle == max) count++;
        return count;
    }
}