package Seminar6.HomeWork.Ex02Notes.Core;

import java.util.List;

public interface FileOperation {
    List<String> readNotes();

    void saveAll(List<String> lines);

}
