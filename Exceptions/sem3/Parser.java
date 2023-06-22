package sem3.hw;

import java.io.*;
import java.util.Scanner;

public class Parser {
    public static void main(String[] args) {
        Data data = new Data();
        data.InputData();
        data.WriteToFile();
    }
}

class Data {
    private String data;
    private String[] dataArray;
    private final int countData = 6;

    public void InputData(){
        Scanner scanner = new Scanner(System.in);

        int res;
        do {
            System.out.println("\"Enter the last name, first name, patronymic, date of birth (format is: dd.mm.yyyy), phone number (11 digits without any separators) and gender (f or m), separated by a SPACE");
            this.data = scanner.nextLine();
            res = CheckQuantity();
            if(res == -1){
                System.out.println("Not all data entered.");
            }
            if (res == -2) {
                System.out.println("too much data entered");
            }

            try {
                ParseData();
            } catch (InputException e) {
                e.printStackTrace();
                res = -3;
            }
        }

        while(res < 0);
        scanner.close();
    }

    private void ParseData() throws InputException{
        if (!dataArray[0].matches("[a-zA-Zа-яёА-ЯЁ]+")){
            throw new InputException("Surname {" + dataArray[0] + "} must contain only letters");
        }
        if (!dataArray[1].matches("[a-zA-Zа-яёА-ЯЁ]+")){
            throw new InputException("Firstname {" + dataArray[1] + "} must contain only letters");
        }
        if (!dataArray[2].matches("[a-zA-Zа-яёА-ЯЁ]+")){
            throw new InputException("Middlename {" + dataArray[2] + "} must contain only letters");
        }
        if (!dataArray[3].matches("\\d{2}\\.\\d{2}\\.\\d{4}")){
            throw new InputException("The wrong bithdate entered {" + dataArray[3] + "}");
        }
        if (!dataArray[4].matches("\\d{11}")){
            throw new InputException("The wrong phone number entered {" + dataArray[4] + "}");
        }
        if (!dataArray[5].matches("[fm]")){
            throw new InputException("The wrong gender entered {" + dataArray[5] + "}");
        }
    }

    private int CheckQuantity() {
        dataArray = data.split("\\s+");
        if (dataArray.length < this.countData){
            return -1;
        }
        if (dataArray.length > this.countData){
            return -2;
        }
        return 0;
    }

    public void WriteToFile(){
        try(FileWriter writer = new FileWriter(dataArray[0]+".txt", true)) {
            data = String.join(" ", dataArray) + "\n";
            writer.write(data);
            System.out.println("The record was successfully written to the file "+ dataArray[0] + ".txt");
        }
        catch(IOException e){
            System.out.println("File writing error");
            e.getStackTrace();
        }
    }
}

class InputException extends Exception{//Runtime

    public InputException(String e) {super(e);}
}
