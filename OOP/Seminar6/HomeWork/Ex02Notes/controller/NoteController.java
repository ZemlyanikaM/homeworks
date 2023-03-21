package Seminar6.HomeWork.Ex02Notes.controller;

import Seminar6.HomeWork.Ex02Notes.Core.Note;
import Seminar6.HomeWork.Ex02Notes.Core.Repository;
import java.util.List;

public class NoteController {
    private  Repository repo;
    public NoteController(Repository repository) {
        this.repo = repository;
    }
    public void saveNote(Note note) throws Exception {
        repo.createNote(note);
    }
    public Note noteRead(String id)  {
        return repo.readNote(id);
    }

    public void exit(){
        repo.exit();
    }

    public List<Note> readAll() {
        return repo.getAllNotes();
    }

    public void noteUpdate(String id, Note updatedNote) throws Exception {
        updatedNote.setId(id);
        repo.updateNote(updatedNote);
    }
    public void noteDelete(String id) {
        Note note = repo.getAllNotes().stream().filter(n -> n.getId().equals(id)).findFirst().orElse(null);
        System.out.println(note);
        repo.deleteNote(note);
    }
    public boolean checkId(String id) throws Exception {
        List<Note> notes = repo.getAllNotes();
        Note note = notes.stream().filter(n -> n.getId().equals(id)).findAny().orElse(null);
        if (note == null)
            throw new Exception("There's no note with Id: " + id);
        return true;
    }
    public boolean checkNotes() {
        List<Note> notes = repo.getAllNotes();
        boolean result = (notes.size() != 0);
        if (!result)
            System.out.println("There're no any note");
        return result;
    }
}
