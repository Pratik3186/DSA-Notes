package Java;

public class PassingInfo {
    static void addNumbers(int num1, int num2){
        int sum = num1 + num2;
        System.out.println("The sum is:" + sum);
    }
    public static void main(String[] args){
        addNumbers(5,10);
        addNumbers(55,3);

    }
}

