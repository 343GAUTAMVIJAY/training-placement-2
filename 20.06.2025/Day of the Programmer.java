public class Solution {
    public static String dayOfProgrammer(int year) {
        if (year == 1918) return "26.09.1918";
        boolean isLeap = year < 1918 ? year % 4 == 0 : 
                        (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
        return isLeap ? "12.09." + year : "13.09." + year;
    }
}