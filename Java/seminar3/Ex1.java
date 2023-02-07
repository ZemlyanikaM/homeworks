//1. Пусть дан произвольный список целых чисел, удалить из него четные числа (в языке уже есть что-то готовое для этого)
package seminar3;
import java.util.ArrayList;
import java.util.Random;
public class Ex1 {
    static Random rnd = new Random();
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        System.out.println(getRandomList(list).toString());
        System.out.println(removeEvenValuesFromList(list).toString());
    }
    public static ArrayList<Integer> getRandomList(ArrayList<Integer> list){
        int length = rnd.nextInt(5, 21);
        for (int i = 0; i <length ; i++) {
            list.add(rnd.nextInt(100));
        }
        return list;
    }
    private static ArrayList<Integer> removeEvenValuesFromList(ArrayList<Integer> list){
        list.removeIf(n -> (n % 2 == 0));
        return list;
    }
}
