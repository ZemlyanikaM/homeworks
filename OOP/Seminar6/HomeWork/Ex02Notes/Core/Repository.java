package Seminar6.HomeWork.Ex02Notes.Core;

import java.util.List;

public interface Repository {
    List<Note> getAllNotes();
    void createNote(Note note);
    void updateNote(Note note);
    void deleteNote(Note note);
    Note readNote(String id);
    void exit();


}
