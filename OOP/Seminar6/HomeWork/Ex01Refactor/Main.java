package Seminar6.HomeWork.Ex01Refactor;

import Seminar6.HomeWork.Ex01Refactor.Persister.SaveToNoWhere;
import Seminar6.HomeWork.Ex01Refactor.Reporter.ScreenReporter;
import Seminar6.HomeWork.Ex01Refactor.User.UserType1;

public class Main{
	public static void main(String[] args){
		UserType1 user = new UserType1("Bob");
		ScreenReporter report = new ScreenReporter();
		SaveToNoWhere persister = new SaveToNoWhere(user);
		report.report(user);
		persister.save();
	}
}