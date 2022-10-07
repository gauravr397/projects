import java.util.Scanner;

public class guessit {
    public static void main(String[] args) {
        int mynumb = (int) (Math.random() * 100);
        Scanner sc = new Scanner(System.in);
        int usernumb = 0;

        do {
            System.out.println("Guess my number :");
            usernumb = sc.nextInt();

            if (usernumb == mynumb) {
                System.out.println("Great work , chief !! ....CORRECT NUMBER ");
                break;
            } else if (usernumb > mynumb) {
                System.out.println("number too large ");
            } else {
                System.out.println("number too small");
            }
        } while (usernumb >= 0);
        System.out.println("my number was :" + mynumb);

    }
}