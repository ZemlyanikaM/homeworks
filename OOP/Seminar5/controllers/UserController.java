package Seminar5.controllers;

import Seminar5.model.Repository;
import Seminar5.model.User;
import Seminar5.model.ValidateUser;

import java.util.List;

public class UserController {
    private final Repository repository;

    private ValidateUser validator = new ValidateUser();

    public UserController(Repository repository) {
        this.repository = repository;
    }

    public void saveUser(User user) throws Exception {
        validator.check(user);
        repository.createUser(user);
    }

    public User readUser(String userId) throws Exception {
        List<User> users = repository.getAllUsers();
        for (User user : users) {
            if (user.getId().equals(userId)) {
                return user;
            }
        }

        throw new Exception("User not found");
    }

    public List<User> readUsers() {
        List<User> users = repository.getAllUsers();
        return users;
    }

    public void deleteUser(String userId) {
        repository.deleteUser(userId);
    }


    public void updateUser(String userId,String firstName, String lastName, String phone) throws Exception {
        try {
            User user = this.readUser(userId);
            repository.updateUser(user, userId, firstName, lastName, phone);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

    }
}
