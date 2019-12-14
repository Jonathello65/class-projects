//Jonathan Wright
//CIS150-401
//This program will accept 5 grades between 0-100 and output the highest grade,
//lowest grade, and average.

package programs;

import java.util.Scanner;

public class Exam1 {
	public static void main(String[] args) {
		
		//Initializes an array with 5 spots for each grade
		int[] grades = new int[5];
		
		Scanner input = new Scanner(System.in);
		
		//Initializes variables to be used in the loop
		int count = 1;
		int grade = 0;
		
		//Asks user for five grades, adding them to the array if between 0-100
		//or repeating the prompt if out of range
		while (count < 6) {
			grade = 0;
			System.out.println("Enter grade " + count + " of 5 (0-100)");
			grade = input.nextInt();
			if (grade < 0 || grade > 100) {
				continue;
			} else {
				grades[count - 1] = grade;
				count += 1;
			}
		}
		
		System.out.println("");
		
		//Displays the grades that have been entered
		System.out.println("Grades entered:");
		for (int i = 0; i < 5; i++) {
			System.out.print(grades[i] + " ");
		}
		
		System.out.println("\n");
		
		//Calls the other functions to display the highest, lowest, and average
		System.out.println("Highest grade: " + highest(grades));
		System.out.println("Lowest grade: " + lowest(grades));
		System.out.println("Average grade: " + average(grades));
	}
	
	//Goes through the array and returns the highest grade
	public static int highest(int[] grades) {
		int max = 0;
		for (int i = 0; i < 5; i++) {
			if (grades[i] > max) {
				max = grades[i];
			}
		}
		return max;
	}
	
	//Goes through the array and returns the lowest grade
	public static int lowest(int[] grades) {
		int min = 100;
		for (int i = 0; i < 5; i++) {
			if (grades[i] < min) {
				min = grades[i];
			}
		}
		return min;
	}
	
	//Sums up the values in the array and returns the average
	public static double average(int[] grades) {
		int sum = 0;
		for (int i = 0; i < 5; i++) {
			sum += grades[i];
		}
		double average = sum / 5.0;
		return average;
	}
}
