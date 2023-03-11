package Seminar6.HomeWork.Ex01Refactor.Persister;

import Seminar6.HomeWork.Ex01Refactor.User.AbstractUser;
import Seminar6.HomeWork.Ex01Refactor.User.UserType1;

public class SaveToNoWhere {
	private AbstractUser savingUser;
	public SaveToNoWhere(UserType1 user) {
			this.savingUser = user;
		}
	public void save(){
		System.out.println("Save user: " + savingUser.getUserName());
	}
}