public class NeonNumber {
    public static void main(String[] args){
        int n = 2;
        int sq = n*n;
        int sum = 0;
        while(sq>0){
            int r = sq%10;
            sum = sum + r;
            sq = sq/10;
        }
        if(sum == n){
            System.out.println("Neon");
        }else{
            System.out.println("Not Neon");
        }
    }
    
}
