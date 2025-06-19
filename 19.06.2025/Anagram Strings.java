import java.util.*;
public class Solution {
    public static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;
        char[] arr1 = a.toLowerCase().toCharArray();
        char[] arr2 = b.toLowerCase().toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }
}