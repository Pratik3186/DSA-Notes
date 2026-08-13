package Java;

public class Nonstatic {
    String breed; //instance variable
    int age;
    public static void main(String[] args){
        Nonstatic myDog = new Nonstatic();
        System.out.println(myDog.breed + "is barking!");

    }
    
}
