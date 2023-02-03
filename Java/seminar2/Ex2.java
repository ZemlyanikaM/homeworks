//Напишите метод, который составит строку, состоящую из 100 повторений слова TEST и метод, который запишет эту строку в простой текстовый файл, обработайте исключения.
package seminar2;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
public class Ex2 {
    public static void main(String[] args) {
        String text = "TEST";
        int count = 100;
        String result = stringMaker(text,count);
        writeStringToFile(result);
    }
    public static String stringMaker(String text, int count){
        return text.repeat(count);
    }
    public static void writeStringToFile(String result){
        try(PrintWriter pw = new PrintWriter("src/main/resources/lib/ex2.txt")) {
            pw.print(result);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

}
