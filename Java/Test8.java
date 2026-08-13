// package Java;
public class Test8 {
    String name;
    static int id;
    public static void main(String[] args){
        Test8 s1 = new Test8();
        Test8 s2 = new Test8();
        s1.name = "Virat";
        s2.name = "Dhobi";
        s2.id  = 7;
        s1.id = 18;
        System.out.println(s1.name + "" + s1.id);
        System.out.println(s2.name + "" + s2.id);       
    }   
}
