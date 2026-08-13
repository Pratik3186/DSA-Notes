// package Java;

public class Test6 {
    static int i = 10;
    public static void main(String[] args)
    {
        System.out.println("main starts");
        System.out.println(i);
        D.m1();
        System.out.println("Main ends");
    }
    
}
class D{
    static int j=10;
    static void m1(){
        System.out.println(j);
    }
}
