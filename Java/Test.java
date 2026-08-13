public class Test{
    int i = 10;
    public static void main(String[] args){
        Test a = new Test();// Creates an object named 'a'
        System.out.println(a.i);//Print 10
        B.m1();
        
    }
}

class B{
    int i = 20;
    public static void m1(){
        B a = new B();
        System.out.println(a.i);
    }

}