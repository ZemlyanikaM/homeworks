package Seminar2;

public class Dog extends Predator implements Runable, Sayable, Swimable{
    public Dog(String nickname) {
        super(nickname);
    }

    public String toString(){
        return "This is a dog. " + super.toString() + ". It's speed is " + speedOfRun()  + ". Speed of swim is " + speedOfSwim();
    }
    public String say(){
        return "gav-gav";
    }
    public int speedOfSwim() {
        return 10;
    }
    @Override
    public int speedOfRun() {
        return 50;
    }
}