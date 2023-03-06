package Seminar4.Game;

import Seminar4.Game.Shields.LightShield;
import Seminar4.Game.Weapons.Ranged;

public class Archer extends BaseHero<Ranged , LightShield>{
    public Archer(int health, String name, Ranged ranged) {
        super(health, name, ranged);

    }

    public Archer(int health, String name, Ranged ranged, LightShield shield) {
        super(health, name, ranged, shield);
    }

    @Override
    public Ranged getWeapon() {
        return super.getWeapon();
    }

    public  int range(){
        return  weapon.getRange();
          }

    @Override
    public String toString() {
        return  "Archer{" + super.toString() + "\n" +  "~~~";
    }
}
