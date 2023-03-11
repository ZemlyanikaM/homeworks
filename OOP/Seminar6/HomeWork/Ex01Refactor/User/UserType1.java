package Seminar6.HomeWork.Ex01Refactor.User;

import Seminar6.HomeWork.Ex01Refactor.Persister.SaveToNoWhere;

public class UserType1 extends AbstractUser {
	public UserType1(String name) {
		super(name);
	}

	public String getName() {
		return super.getUserName();
	}
}