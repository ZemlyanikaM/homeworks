package Seminar2;

public class Cow extends Herbivores implements Runable, Sayable, Swimable{
    public Cow(String nickname) {
        super(nickname);
    }

    public String toString(){
        return "This is a cow. " + super.toString() + ". It's speed is " + speedOfRun()  + ". Speed of swim is " + speedOfSwim();
    }
    public String say(){
        return "Mu-mu";
    }
    public int speedOfSwim() {
        return 7;
    }
    @Override
    public int speedOfRun() {
        return 5;
    }
}