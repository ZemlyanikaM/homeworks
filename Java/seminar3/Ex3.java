//Пройти по списку из задания 2 с урока и удалить повторяющиеся элементы.
package seminar3;
import java.util.*;
public class Ex3 {
    public static void main(String[] args) {
        ex2();
    }
    public static void ex2() {
        List<String> planets = new ArrayList<>();
        HashMap<String, Integer> planetCount = new HashMap<>();
        Random rand = new Random();

        String[] solarSystemPlanets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        for (int i = 0; i < 10; i++) {
            int randIndex = rand.nextInt(solarSystemPlanets.length);
            planets.add(solarSystemPlanets[randIndex]);
        }

        for (String planet : planets) {
            if (planetCount.containsKey(planet)) {
                planetCount.put(planet, planetCount.get(planet) + 1);
            } else {
                planetCount.put(planet, 1);
            }
        }

        for (String planet : planetCount.keySet()) {
            System.out.printf("%s\t%s%n", planet, planetCount.get(planet));
        }
        System.out.println(planets);
        Set<String> planetsSet = new HashSet<>(planets);
        System.out.println(planetsSet);
    }
}
