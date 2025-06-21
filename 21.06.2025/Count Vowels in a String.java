public class VowelCount {
    public static void main(String[] args) {
        String str = "Hello, World!";
        System.out.println("Number of vowels: " + countVowels(str));
    }

    static int countVowels(String str) {
        str = str.toLowerCase();
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        return count;
    }
}