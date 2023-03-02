package Seminar2;

public class Dolphin extends Predator implements Swimable,Sayable {
    public Dolphin(String nickname) {
        super(nickname);
    }

    @Override
    public String say() {
        return "Ultrasound";
    }

    @Override
    public int speedOfSwim() {
        return 35;
    }
    public String toString(){
        return "This is dolphin. " + super.toString() + ". It's speed of swim is " + speedOfSwim();
    }

}
