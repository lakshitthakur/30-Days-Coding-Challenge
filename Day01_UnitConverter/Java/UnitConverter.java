import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Unit Converter:");
        System.out.println("1. cm to inches");
        System.out.println("2. kg to pounds");
        System.out.println("3. Celsius to Fahrenheit");

        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter cm: ");
                double cm = sc.nextDouble();
                System.out.printf("%.2f cm = %.2f inches%n", cm, cm / 2.54);
                break;
            case 2:
                System.out.print("Enter kg: ");
                double kg = sc.nextDouble();
                System.out.printf("%.2f kg = %.2f pounds%n", kg, kg * 2.20462);
                break;
            case 3:
                System.out.print("Enter Celsius: ");
                double c = sc.nextDouble();
                System.out.printf("%.2f °C = %.2f °F%n", c, (c * 9/5) + 32);
                break;
            default:
                System.out.println("Invalid choice.");
        }

        sc.close();
    }
}
