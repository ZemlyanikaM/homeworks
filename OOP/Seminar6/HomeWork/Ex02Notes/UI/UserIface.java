package Seminar6.HomeWork.Ex02Notes.UI;

import Seminar6.HomeWork.Ex02Notes.Core.*;
import Seminar6.HomeWork.Ex02Notes.controller.NoteController;
import java.util.Scanner;

public class UserIface {
    private NoteController noteController;
    public UserIface() {
    }
    public void start() {
        Commands com = Commands.NONE;
        String id;
        String command;
        FileOperation fileOperation;
        Repository repository;
        fileOperation = new FileOperationImpl("notes.txt");
        repository = new RepositoryFile(fileOperation);
        this.noteController = new NoteController(repository);
        NoteController noteController = new NoteController(repository);

        while (true) {
            command = prompt("Enter a command (Create,Read,Update,Delete,List,Exit): ");
            while (!commandValidate(command.toUpperCase())) {
                command = prompt("Enter a command: ");
            }
            com = Commands.valueOf(command.toUpperCase());
            if (com == Commands.EXIT)  {
                noteController.exit();
            return;
            }
            try {
                switch (com) {
                    case CREATE:
                        noteController.saveNote(createNote());
                        break;
                    case READ:
                        if (noteController.checkNotes()) {
                            id = prompt("Enter note's id: ");
                            noteController.checkId(id);
                            try {
                                Note note = noteController.noteRead(id);
                                System.out.println(note);
                            } catch (Exception e) {
                                throw new RuntimeException(e);
                            }
                        }
                        break;
                    case LIST:
                        if (noteController.checkNotes())
                            for (Note item : noteController.readAll()) {
                                System.out.println(item + "\n");
                            }
                        break;
                    case UPDATE:
                        if (noteController.checkNotes()) {
                            id = prompt("Enter id to update note: ");
                            noteController.checkId(id);
                            noteController.noteUpdate(id, createNote());
                        }
                        break;
                    case DELETE:
                        if (noteController.checkNotes()) {
                            id = prompt("Enter id to delete note: ");
                            noteController.checkId(id);
                            noteController.noteDelete(id);
                        }
                        break;
                }
            } catch (Exception e) {
                System.out.println("Error " + e.getMessage());
            }
        }
    }

    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.print(message);
        return in.nextLine();
    }
    private Note createNote() {
        String id = prompt("Id:");
        String title = prompt("Title: ");
        String text = prompt("Content: ");
        return (new Note(id, title, text));
    }
    private boolean commandValidate(String command) {
        try {
            Commands.valueOf(command);
            return true;
        } catch (IllegalArgumentException e) {
            System.out.println("Command not found");
            return false;
        }
    }
}
