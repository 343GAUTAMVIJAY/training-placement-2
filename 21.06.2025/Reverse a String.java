public class ReverseString {
    public static void main(String[] args) {
        String str = "Hello, World!";
        System.out.println("Loop Reverse: " + reverseWithLoop(str));
        System.out.println("StringBuilder Reverse: " + reverseWithStringBuilder(str));
    }

    static String reverseWithLoop(String str) {
        char[] chars = str.toCharArray();
        StringBuilder reversed = new StringBuilder();
        for (int i = chars.length - 1; i >= 0; i--) {
            reversed.append(chars[i]);
        }
        return reversed.toString();
    }

    static String reverseWithStringBuilder(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}