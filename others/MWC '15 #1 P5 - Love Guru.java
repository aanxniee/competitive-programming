/* MWC '15 #1 P5 - Love Guru */

import java.util.*;
public class Main {
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
        // convert both names to lowercase
		String a = sc.next().toLowerCase(); 
		String b = sc.next().toLowerCase();
		int x = 0, y = 0;
		
        // find the value of each name by raising each letter to the power of its position
        // convert letter to its unicode value, pass through method, then mod by 10
		for (int i = 0; i < a.length(); i++) {
			x = (x + pow(a.charAt(i) - 'a' + 1, i + 1, 10)) % 10;
		}
		
		for(int i = 0; i < b.length(); i++) {
			y = (y + pow(b.charAt(i) - 'a' + 1, i + 1, 10)) % 10;
		}
		
		if (x == 0) x = 10;
		if (y == 0) y = 10;
		
        // sum together values of each name for compatibility
		System.out.println(x + y);
		sc.close();
	}
	
    // method to find the total value after raising each letter to the power of its position
	static int pow(int b, int e, int m) {
        // if letter is raised to the power of 1, return its unicode value (base case)
		if (e == 1) return b;
    
		int i = pow(b, e / 2, m); // recursive call
		
		if (e % 2 != 0) return i * i * b % m;
		else return i * i % m;	
	}
}