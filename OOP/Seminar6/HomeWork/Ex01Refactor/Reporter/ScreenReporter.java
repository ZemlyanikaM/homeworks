package Seminar6.HomeWork.Ex01Refactor.Reporter;

import Seminar6.HomeWork.Ex01Refactor.User.AbstractUser;

public class ScreenReporter {
       public void report(AbstractUser user) {
        System.out.println("Report for user: " + user.getUserName());
    }

}
