public class challenge12 {
    public static void main(String[] args){
        int n = 10;
        int a=0,b=1;
        System.out.println("Fibo up to "+n+" terms ");
        for(int i=1;i<=n;i++){
            System.out.print(b+" ");
            int c = a+b;
            a = b;
            b = c;
        }
    }
    
}
