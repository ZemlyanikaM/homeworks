package Seminar6.HomeWork.Ex01Refactor.User;

public abstract class AbstractUser {
    private String userName;

    protected AbstractUser(String userName) {
        this.userName = userName;
    }
    public String getUserName() {
        return this.userName;
    }

}
