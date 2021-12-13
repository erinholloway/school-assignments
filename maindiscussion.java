import java.util.Scanner;

public class maindiscussion {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        System.out.print("Enter the width of the wall in feet:");
        // prompts user to enter width of wall in feet
        double num1 = scan.nextInt();
        System.out.print("Enter the height of the wall in feet: ");
        // prompts user to enter height of wall in feet
        double num2 = scan.nextInt();
   
        double product = num1*num2;
        // calculates square footage 
        double paint = product/350;
        // calculates the average square feet 1 gallon of paint covers
        System.out.println("Total quare footage:" + product);
        System.out.println("Gallons of paint needed:" + paint);
		scan.close();
		// close scanner
	} // close main
} // close class