package Seminar2;

public class Butterfly extends Herbivores implements Flyable{
    public Butterfly(String nickname) {
        super(nickname);

    }

    @Override
    public int speedOfFly() {
        return 10;
    }
    public String toString(){
        return "This is a butterfly. " + super.toString() + ". It's speed is " + speedOfFly();
    }

}