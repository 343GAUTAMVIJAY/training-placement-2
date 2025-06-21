public class Factorial {
    public static void main(String[] args) {
        int num = 5;
        System.out.println("Iterative Factorial: " + factorialIterative(num));
        System.out.println("Recursive Factorial: " + factorialRecursive(num));
    }

    static long factorialIterative(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    static long factorialRecursive(int n) {
        if (n <= 1) return 1;
        return n * factorialRecursive(n - 1);
    }
}