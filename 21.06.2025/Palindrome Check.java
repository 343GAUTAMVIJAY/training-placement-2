public class Palindrome {
    public static void main(String[] args) {
        String str = "radar";
        System.out.println(str + " is palindrome: " + isPalindrome(str));
    }

    static boolean isPalindrome(String str) {
        str = str.toLowerCase().replaceAll("[^a-z0-9]", "");
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left++) != str.charAt(right--)) return false;
        }
        return true;
    }
}