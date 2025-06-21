import java.util.Scanner;

public class TemperatureConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter temperature value: ");
        double temp = scanner.nextDouble();
        System.out.print("Enter unit (C/F/K): ");
        char unit = scanner.next().toUpperCase().charAt(0);
        
        if (unit == 'C') {
            System.out.println("Fahrenheit: " + (temp * 9/5 + 32));
            System.out.println("Kelvin: " + (temp + 273.15));
        } else if (unit == 'F') {
            System.out.println("Celsius: " + ((temp - 32) * 5/9));
            System.out.println("Kelvin: " + ((temp - 32) * 5/9 + 273.15));
        } else if (unit == 'K') {
            System.out.println("Celsius: " + (temp - 273.15));
            System.out.println("Fahrenheit: " + ((temp - 273.15) * 9/5 + 32));
        } else {
            System.out.println("Invalid unit!");
        }
        scanner.close();
    }
}