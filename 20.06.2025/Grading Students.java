import java.util.*;
public class Solution {
    public static List<Integer> gradingStudents(List<Integer> grades) {
        List<Integer> result = new ArrayList<>();
        for (int grade : grades) {
            if (grade < 38) result.add(grade);
            else {
                int nextMultiple = ((grade / 5) + 5 - grade % 5;
                result.add(grade >= 38 && diff < 3 ? nextMultiple : grade);
            }
        }
        return result;
    }