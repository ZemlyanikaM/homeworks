package Seminar5.model;

import java.util.List;

public interface Repository {
    List<User> getAllUsers();
    String createUser(User user);

    void deleteUser(String userId);

    void updateUser(User user,String userId,String firstName, String lastName, String phone);
}
