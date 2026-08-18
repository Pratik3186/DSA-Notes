public class Challenge3 {
    static int count = 0;

    public Challenge3() {
        count++;
    }

    public static void main(String[] args) {
        Challenge3 s1 = new Challenge3();
        s1.count = 5;

        Challenge3 s2 = new Challenge3();

        System.out.println(s1.count);
        System.out.println(s2.count);
    }
}