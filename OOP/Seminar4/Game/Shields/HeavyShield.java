package Seminar4.Game.Shields;

import Seminar4.Game.Shield;

public class HeavyShield implements Shield {
    String shieldName;
    private int defendPoints;
    public int getDefendPoints() {
        return defendPoints;
    }
    public HeavyShield(String shieldName, int defendPoints) {
        this.shieldName = shieldName;
        this.defendPoints = defendPoints;
    }
    @Override
    public int Defend() {
        return defendPoints;
    }
    @Override
    public String toString() {
        return "Shield{" +
                "shieldName='" + shieldName + '\'' +
                ", defendPoints=" + defendPoints +
                '}';
    }
}
