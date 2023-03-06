package Seminar4.Game;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class Team<T extends BaseHero> implements Iterable<T> {
    List<T> dreamTeam = new ArrayList<T>();
    public void add(T t) {
        dreamTeam.add(t);
    }

    @Override
    public Iterator<T> iterator() {
        return dreamTeam.iterator();
    }
    public T weakestShield(){
        T weakest = null;
        for (T warrior : dreamTeam) {
            if (warrior.isHasShield()) {
                if (weakest == null) {
                    weakest = warrior;
                } else {
                    if (weakest.shield.Defend() > warrior.shield.Defend()) {
                        weakest = warrior;
                    }
                }
            }

        }
        return weakest;
    }
    public int getTeamHealth() {
        int teamHealth = 0;
        for (T hero : dreamTeam) {
            teamHealth += hero.getHealth();
        }
        return teamHealth;
    }

    public int getMaxRange() {

        int maxRange = 0;
        for (T hero : dreamTeam) {

            if (hero instanceof Archer) {

                Archer archer = (Archer) hero;

                if (maxRange < archer.range()) {

                    maxRange = archer.range();
                }
            }

        }

        return maxRange;
    }

    public int getSumDamage() {

        int sumDamage = 0;

        for (T hero : dreamTeam) {

            sumDamage += hero.getWeapon().damage();

        }

        return sumDamage;
    }



}
