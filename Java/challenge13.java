public class challenge13 {
    public static void main(String[] args){
        int n = 10;
        int a = 0, b = 0, c = 1;
        System.out.print("Fibo up to"+n+"terms");
        for( int i = 0;i<=n;i++){
            System.out.print(a + " ");
            int sum = a+b+c;
            a = b;
            b = c;
            c = sum;
        }

    }
    
}
