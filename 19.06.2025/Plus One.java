public class Solution {
    public static List<Integer> plusOne(List<Integer> digits) {
        List<Integer> result = new ArrayList<>(digits);
        int n = result.size();
        for (int i = n - 1; i >= 0; i--) {
            if (result.get(i) < 9) {
                result.set(i, result.get(i) + 1);
                return result;
            }
            result.set(i, 0);
        }
        result.add(0, 1);
        return result;
    }
}