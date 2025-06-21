import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        System.out.print("Enter operator (+, -, *, /): ");
        char operator = scanner.next().charAt(0);

        switch (operator) {
            case '+': System.out.println(num1 + " + " + num2 + " = " + (num1 + num2)); break;
            case '-': System.out.println(num1 + " - " + num2 + " = " + (num1 - num2)); break;
            case '*': System.out.println(num1 + " * " + num2 + " = " + (num1 * num2)); break;
            case '/': 
                if (num2 != 0) System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
                else System.out.println("Division by zero is not allowed.");
                break;
            default: System.out.println("Invalid operator!");
        }
        scanner.close();
    }
}