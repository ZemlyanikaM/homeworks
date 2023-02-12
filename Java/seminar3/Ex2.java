//Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее арифметическое из этого списка.
package seminar3;
import java.util.ArrayList;

public class Ex2 {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list = Ex1.getRandomList(list);
        System.out.println(list);
        int max = list.stream().max(Integer::compare).get();
        System.out.println(max);
        int min = list.stream().min(Integer::compare).get();
        System.out.println(min);
        System.out.println(findAverageValue(list));
    }
    private static double findAverageValue(ArrayList<Integer> list){
        double mean = 0;
        for (int value : list) {
            mean += value;
        }
        mean = mean/list.size();
        return mean;
    }
}
