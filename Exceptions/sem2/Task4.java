/*
Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
 */
package sem2.hw;


import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) throws Exception {
        System.out.println("Enter a string: ");
        Scanner scanner = new Scanner(System.in);
        String data = scanner.nextLine();
        if (data.equals("")) {
            throw new Exception("Error! An empty string has been entered!");
        } else {
            System.out.println(data);
        }
    }
}