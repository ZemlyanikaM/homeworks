//Пусть дан LinkedList с несколькими элементами. Реализуйте метод, который вернет “перевернутый” список.
package seminar4;
import java.util.Iterator;
import java.util.Random;
import java.util.LinkedList;

public class Ex2 {
    public static void main(String[] args) {
        Random rnd = new Random();
        LinkedList<Integer> ll = new LinkedList<>();
        for (int i = 0; i < rnd.nextInt(3,10); i++) {
            ll.add(rnd.nextInt(10));
        }
        System.out.println(ll);
        System.out.println(reverseLl(ll));
    }
    private static LinkedList<Integer> reverseLl(LinkedList<Integer> ll){
        LinkedList<Integer> reversedll = new LinkedList<>();
        int count = ll.size();
        for (int i = 0; i < count; i++) {
            int value = ll.removeLast();
            reversedll.addLast(value);
        }
        return reversedll;
    }
}
