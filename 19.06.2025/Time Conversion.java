import java.util.*;
public class Solution {
    public static String timeConversion(String s) {
        String[] time = s.split(":");
        int hour = Integer.parseInt(time[0]);
        String period = time[2].substring(2);
        if (period.equals("PM") && hour != 12) hour += 12;
        if (period.equals("AM") && hour == 12) hour = 0;
        return String.format("%02d:%s:%s", hour, time[1], time[2].substring(0, 2));
    }
}