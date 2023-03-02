package Seminar2;

public abstract class Animal {
    public String nickname;

    public Animal(String nickname) {
        this.nickname = nickname;
    }

    public abstract String feed();

    public String toString() {
        return "It's nickname is " + nickname;
    }
}