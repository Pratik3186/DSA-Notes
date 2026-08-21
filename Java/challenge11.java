public class challenge11 {
    public static void main(String[] args){
        int n = 10;
        int a = 0, b = 0, c = 1;
        System.out.print("Tribonaci series of " + n);
        for(int i = 1; i<=n; i++){
            System.out.print(a+" ");
            int nextTerm = a+b+c;
            a = b;
            b = c;
            c = nextTerm;
        }
    }  
}
