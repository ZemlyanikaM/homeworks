package seminar6;
import seminar6.Laptop;
import java.util.List;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {

        Laptop lpt1 = new Laptop("MSI Katana GF76","Intel Core i5-11400H",16, "GeForce GTX 1650 4 ГБ + Intel UHD Graphics", "SSD",
                512, 17.3, "IPS", 53, "none", "MSI");
        Laptop lpt2 = new Laptop("HUAWEI MateBook D 15","AMD Ryzen 5 5500U",8, "AMD Radeon Graphics", "SSD",
                256, 15.6, "IPS", 42, "Windows 11", "Huawei");
        Laptop lpt3 = new Laptop("ASUS VivoBook PRO 15","AMD Ryzen 5 5600H",8, "GeForce GTX 1650 + AMD Radeon Graphics", "SSD",
                512, 15.6, "IPS", 50, "none", "Asus");
        Laptop lpt4 = new Laptop("GIGABYTE G5 GE","Intel Core i5-12500H",16, "GeForce RTX 3050 + Intel UHD Graphics", "SSD",
                512, 15.6, "IPS", 49, "none", "Gigabyte");
        Laptop lpt5 = new Laptop("Apple MacBook Pro","Apple M1 Pro",16, "Apple M1 Pro 14-core", "SSD",
                512, 14.2, "mini-LED", 70, "macOS", "Apple");
        Laptop lpt6 = new Laptop("Apple MacBook","Apple M1 Pro",32, "Apple M1 Pro 14-core", "SSD",
                512, 14.2, "mini-LED", 70, "macOS", "Apple");

        List<Laptop> notebooks = List.of(lpt1,lpt2,lpt3,lpt4,lpt5,lpt6);
        Scanner readLine = new Scanner(System.in);
        System.out.printf("Enter a Brand name:");
        String usersBrandName = readLine.next();
        int count = -1;
        for (Laptop item : notebooks) {
            if (item.getBrand().equals(usersBrandName)){
                System.out.println(item);
                count++;
            }
        }
        if (count < 0){
            System.out.printf("There are no any laptop from %s", usersBrandName);
        }
    }


}