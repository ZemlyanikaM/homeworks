/*
Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
вместо этого, необходимо повторно запросить у пользователя ввод данных.
*/

package sem2.hw;

import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        float num = prompt();
        System.out.println(num);
    }
    public static float prompt() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a fractional number: ");
        while (!scanner.hasNextFloat()) {
            scanner.nextLine();
            System.out.print("Wrong input! Enter a fractional number: ");
        }
        return scanner.nextFloat();
    }
}