package Seminar4.Game.Shields;
import Seminar4.Game.Shield;
public class LightShield implements Shield {
    String shieldName;
    private int defendPoints;
    public LightShield(String shieldName, int defendPoints) {
        this.shieldName = shieldName;
        this.defendPoints = defendPoints;
    }
    @Override
    public int Defend() {
        return defendPoints;
    }
    public int getDefendPoints() {
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
