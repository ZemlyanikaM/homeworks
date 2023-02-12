package seminar1;
// Задать одномерный массив и найти в нем минимальный и максимальный элементы
import java.util.*;

public class Ex1 {
    public static void main(String[] args) {
        ArrayList<Integer> col = new ArrayList<Integer>();
        Random rnd = new Random();
        int length = rnd.nextInt(100);
        for (int i = 0; i<length; i++){
            col.add(rnd.nextInt(999));
        }
        int max = Collections.max(col);
        int min = Collections.min(col);
        System.out.printf("Максимальный элемент: " + max + "\nМинимальный элемент: " + min);
    }

}

