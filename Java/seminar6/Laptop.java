package seminar6;

public class Laptop {
    private String name;
    private String cpu;
    private int ram;
    private String gpu;
    private String storageType;
    private int stotageVolume;
    private double screensize;
    private String screenType;
    private int battery;
    private String os;
    private String brand;

    public Laptop(String name, String cpu, int ram, String gpu, String storageType, int stotageVolume, double screensize,
                  String screenType, int battery, String os, String brand) {
        this.name = name;
        this.cpu = cpu;
        this.ram = ram;
        this.gpu = gpu;
        this.storageType = storageType;
        this.stotageVolume = stotageVolume;
        this.screensize = screensize;
        this.screenType = screenType;
        this.battery = battery;
        this.os = os;
        this.brand = brand;
    }


    @Override
    public String toString() {
       return String.format("Brand: %s\nName: %s\nOperating system: %s\nCPU: %s\nGPU: %s\nStorage: %s %dGB\nScreen: %.1f,%s\nBattary: %d WTh\n---------",
               brand, name, os, cpu,gpu,storageType,stotageVolume, screensize,screenType, battery);
    }
    public String getCpu() {
        return cpu;
    }

    public int getRam() {
        return ram;
    }

    public String getGpu() {
        return gpu;
    }

    public String getStorageType() {
        return storageType;
    }

    public int getStotageVolume() {
        return stotageVolume;
    }

    public double getScreensize() {
        return screensize;
    }

    public String getScreenType() {
        return screenType;
    }

    public int getBattery() {
        return battery;
    }

    public String getOs() {
        return os;
    }

    public String getBrand() {
        return brand;
    }

}
