// package Java;
public class Test4 {
    static int i = 10; // static method
    public static void main(String[] args)
    {
        System.out.println("Main starts");
        System.out.println("i");
        D.m1();
        D.m1();
        System.out.println("main starts");
    }   
}
class D 
{
    static int j = 20;
    static void m1(){
        System.out.println(j);
    }
}
