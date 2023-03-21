package Seminar6.HomeWork.Ex02Notes.Core;
import java.util.ArrayList;
import java.util.List;

public class RepositoryFile implements Repository {
    private NoteMapper mapper = new NoteMapper();
    private FileOperation fileOperation;
    public RepositoryFile(FileOperation fileOperation) {
        this.fileOperation = fileOperation;
    }
    @Override
    public List<Note> getAllNotes() {
        List<String> lines = fileOperation.readNotes();
        lines.removeIf(n-> n.equals(""));
        List<Note> notes = new ArrayList<>();
        for (String line : lines) {
            notes.add(mapper.map(line));
        }
        return notes;
    }
    @Override
    public Note readNote(String id) {
        List<Note> notes = getAllNotes();
        return notes.stream().filter(n-> n.getId().equals(id)).findFirst().orElse(null);
    }
    @Override
    public void exit() {
    }
    @Override
    public void createNote(Note note) {
        List<Note> notes = getAllNotes();
            int max = 0;
            for (Note item : notes) {
                int id = Integer.parseInt(item.getId());
                if (max < id) {
                    max = id;
                }
            }
            int newId = max + 1;
            String id = String.format("%d", newId);
            note.setId(id);
            notes.add(note);
        writeToFile(notes);
    }
    @Override
    public void updateNote(Note updatedNote) {
        List<Note> notes = getAllNotes();
        Note operatingNote = notes.stream().filter(n -> n.getId().equals(updatedNote.getId())).findFirst().orElse(null);
        if (operatingNote != null){
            operatingNote.setTitle(updatedNote.getTitle());
            operatingNote.setText(updatedNote.getText());
            writeToFile(notes);
        }
        else System.out.println("There is no note's Id" + updatedNote.getId());
    }
    @Override
    public void deleteNote(Note note) {
        List<Note> notes = getAllNotes();
        notes.removeIf(n -> n.getId().equals(note.getId()));
        writeToFile(notes);
    }
    private void writeToFile(List<Note> notes){
        List<String> lines = new ArrayList<>();
        for (Note item: notes) {
            lines.add(mapper.map(item));
        }
        fileOperation.saveAll(lines);
    }
}
