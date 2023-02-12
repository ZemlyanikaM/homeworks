/**
 * Пусть дан список сотрудников:Иван Иванов
 * Светлана Петрова
 * Кристина Белова
 * Анна Мусина
 * Анна Крутова
 * Иван Юрин
 * Петр Лыков
 * Павел Чернов
 * Петр Чернышов
 * Мария Федорова
 * Марина Светлова
 * Мария Савина
 * Мария Рыкова
 * Марина Лугова
 * Анна Владимирова
 * Иван Мечников
 * Петр Петин
 * Иван Ежов
 * Написать программу, которая найдет и выведет повторяющиеся имена с количеством повторений. Отсортировать по убыванию популярности.
 */
package seminar5;

import java.util.*;

public class Ex2 {
    public static void main(String[] args) {
        ArrayList<String> peoples = new ArrayList<>();
        peoples.add("Иван Иванов");
        peoples.add("Светлана Петрова");
        peoples.add("Кристина Белова");
        peoples.add("Анна Мусина");
        peoples.add("Анна Крутова");
        peoples.add("Иван Юрин");
        peoples.add("Петр Лыков");
        peoples.add("Павел Чернов");
        peoples.add("Петр Чернышов");
        peoples.add("Мария Федорова");
        peoples.add("Марина Светлова");
        peoples.add("Мария Савина");
        peoples.add("Мария Рыкова");
        peoples.add("Марина Лугова");
        peoples.add("Анна Владимирова");
        peoples.add("Иван Мечников");
        peoples.add("Петр Петин");
        peoples.add("Иван Ежов");

        HashMap<String, Integer> names = new HashMap<>();
        HashMap<String, Integer> sortednames = new LinkedHashMap<>();
        String[] people;
        for (String text:peoples) {
            people = text.split("\\s+");
            if (names.containsKey(people[0])){
                names.put(people[0], (names.get(people[0])+1));
          }else {
                names.put(people[0], 1);
            }
        }

        int maxcount = 1;
        for (int value: names.values()) {
            if (value > maxcount) {
                maxcount = value;
            }
        }
        for (int i = maxcount; i > 1 ; i--) {
            for (Map.Entry<String,Integer> entry: names.entrySet()) {
                String key = entry.getKey();
                if (names.get(key) == i){
                    sortednames.put(key,names.get(key));
                }
            }
        }
        System.out.println(names);

        System.out.println(sortednames);
    }


}