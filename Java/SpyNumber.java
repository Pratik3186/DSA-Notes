public class SpyNumber {
    public static void main(String[] args){
        int n = 126;
        int m = n;
        int sum = 0;
        int product = 1;
        while(n>0){
            int r = n%10;
            sum = sum + r;
            product = product*r;
            n=n/10;

        }
        if (sum == product){
            System.out.println(m+" is a spy Number");
        }else{
            System.out.println(m+ " is not a Spy number ");
        }
    }
    
}
