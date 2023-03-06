package Seminar4.Game;


import Seminar4.Game.Shields.HeavyShield;
import Seminar4.Game.Shields.LightShield;
import Seminar4.Game.Weapons.Melee;
import Seminar4.Game.Weapons.Ranged;
import org.w3c.dom.html.HTMLOptGroupElement;

public class Main {

    public static void main(String[] args) {
        Team<BaseHero> shieldTeam = new Team<>();

        shieldTeam.add(new Archer(50, "A1", new Ranged("crossbow", 15, 25),new LightShield("LightShield",15)));
        shieldTeam.add(new Footman(55, "F1", new Melee("sword", 30), new HeavyShield("BigShied" , 30)));
        shieldTeam.add(new Footman(55, "F2", new Melee("knifes", 20), new HeavyShield("SmallShied" , 20)));
        shieldTeam.add(new Archer(50, "A2", new Ranged("bow", 5, 50)));
        shieldTeam.add(new Footman(55, "F3", new Melee("hammer", 50)));


        for (BaseHero item : shieldTeam) {
            System.out.println(item);
        }
        System.out.printf("The weakest shield is:  " + shieldTeam.weakestShield());


//        Team<Footman> squadF = new Team<>();
//
//        squadF.add(new Footman(55, "joe", new Melee("spear", 15)));
//        squadF.add(new Footman(55, "moe", new Melee("sword", 10)));
//        squadF.add(new Footman(55, "doe", new Melee("axe", 20)));
//
//        for (Footman item : squadF) {
//            System.out.println(item);
//        }
//
//        System.out.println(squadF.getTeamHealth());
//        System.out.println(squadF.getMaxRange());
//        System.out.println(squadF.getSumDamage());
//
//        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
//
//        Team<BaseHero> squadA = new Team<>();
//
//        squadA.add(new Archer(15, "jonh", new Ranged("bow", 5, 50)));
//        squadA.add(new Archer(15, "jonathan", new Ranged("crossbow", 15, 25)));
//        squadA.add(new Footman(55, "carl", new Melee("sword", 10)));
//        squadA.add(new Footman(55, "earl", new Melee("axe", 20)));
//
//        for (BaseHero item : squadA) {
//            System.out.println(item);
//        }
//
//        System.out.println(squadA.getTeamHealth());
//        System.out.println(squadA.getMaxRange());
//        System.out.println(squadA.getSumDamage());
//
//        Footman footman1 = new Footman(77 , "marks" , new Melee("book"  , 30));
//        Footman footman2 = new Footman(66 , "adamS" , new Melee("weights"  , 45));
//        while (footman1.getHealth()>0 && footman2.getHealth()> 0){
//            footman1.hit(footman2);
//            System.out.println(footman2);
//            System.out.println("~~~~~~~~");
//            footman2.hit(footman1);
//            System.out.println(footman1);
//            System.out.println("____________");
//
//
//        }
//        if (footman1.getHealth()>0){
//            System.out.println(footman1 + " is Winner");
//        }
//        else {
//            System.out.println(footman2 + " is Winner");
//        }

    }

}
