import java.util.Scanner;
public class CountDigit {
    public static int CountofNumber(int n){
        // Scanner scn = new Scanner(System.in);
        // System.out.println("The count of number is: ");
        // int a = scn.nextInt();
        int count =  0;
        while(n>0){
            count++;
            n = n/10;
        }
        return count; 
    }
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = scn.nextInt();
        int result = CountofNumber(n);
        System.out.println("The count of a digit is: "+ result);
        scn.close();

    }
    
}

