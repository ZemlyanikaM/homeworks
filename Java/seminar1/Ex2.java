package seminar1;
import java.util.Random;
//Написать метод, который определяет, является ли год високосным, и возвращает boolean (високосный - true, не високосный - false). Каждый 4-й год является високосным, кроме каждого 100-го, при этом каждый 400-й – високосный.
public class Ex2 {
    public static void main(String[] args) {
        Random rnd = new Random();
        int year = rnd.nextInt(2023);
        System.out.println(year);
        System.out.println(checkLeapYear(year));
    }
    private static boolean checkLeapYear(int year){
        return ((year %4 ==0) && (year % 100 !=0) || (year %4 ==0) && (year %400 ==0));


    }
}
