import java.util.*;
public class Solution {
    public static List<Integer> countingSort(List<Integer> arr) {
        List<Integer> result = new ArrayList<>(Collections.nCopies(100, 0));
        for (int num : arr) result.set(num, result.get(num) + 1);
        return result;
    }
}