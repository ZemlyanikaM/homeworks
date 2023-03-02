package Seminar2;

public class Rabbit extends Herbivores implements Runable, Swimable {
    public Rabbit (String nickname) {
        super(nickname);
    }

    public String toString(){
        return "This is a rabbit. " + super.toString() + ". It's speed is " + speedOfRun()
                + ". Speed of swim is " + speedOfSwim();
    }
    public String say(){
        return "kdfgk";
    }
    public int speedOfSwim() {
        return 5;
    }
    @Override
    public int speedOfRun() {
        return 30;
    }
}