import java.util.*;
public class Solution {
    public static List<Integer> matchingStrings(List<String> strings, List<String> queries) {
        List<Integer> results = new ArrayList<>();
        for (String query : queries) {
            int count = 0;
            for (String str : strings) {
                if (str.equals(query)) count++;
            }
            results.add(count);
        }
        return results;
    }
}