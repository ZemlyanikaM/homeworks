package Seminar2;
public class Duck extends Herbivores implements Flyable, Runable, Sayable, Swimable{
    public Duck(String nickname) {
        super(nickname);

    }

    @Override
    public int speedOfFly() {
        return 50;
    }
    public String toString(){
        return "This is a duck. " + super.toString() + ". It's speed is " + speedOfRun() + ", speed of fly "
                + speedOfFly() + ". Speed of swim is " + speedOfSwim();
    }
    @Override
    public int speedOfRun() {
        return 5;
    }
    public int speedOfSwim() {
        return 10;
    }
    @Override
    public String say() {
        return "Krya-krya";
    }
}