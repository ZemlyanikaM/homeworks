package Seminar4.Game;

import Seminar4.Game.Shields.HeavyShield;
import Seminar4.Game.Shields.LightShield;
import Seminar4.Game.Weapons.Melee;

public class Footman extends BaseHero<Melee, HeavyShield> {

    public Footman(int health, String name, Melee weapon) {
        super(health, name, weapon);
    }

    public Footman(int health, String name, Melee weapon, HeavyShield shield) {
        super(health, name, weapon, shield);
    }

    @Override
    public String toString() {
        return "Footman{" +
                "} " + super.toString() + "\n" +  "~~~";
    }
}
