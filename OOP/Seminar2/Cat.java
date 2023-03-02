package Seminar2;

public class Cat extends Predator implements Runable, Sayable, Swimable{
    public Cat(String nickname) {
        super(nickname);
    }

    public String toString(){
        return "This is a cat. " + super.toString() + ". It's speed is " + speedOfRun()  + ". Speed of swim is " + speedOfSwim();
    }
    public String say(){
        return "meow-meow";
    }
    public int speedOfSwim(){
        return 5;
    }
    @Override
    public int speedOfRun() {
        return 10;
    }
}