// package Java;

public class Test5 {
    static int i;
    int j; // non static variable
    public static void main(String[] args)
    {
        System.out.println(i);
        Test5 adr1 = new Test5();
        System.out.println(adr1.j);
        // Test5 adr2 = new Test5();
        // System.out.println(adr2.j);
    }
    
}
