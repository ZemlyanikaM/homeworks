package sem1.hw;

public class task1 {
    public static void main(String[] args) {
        String[] arr = {"1","w","world","f"};
        func1(arr);
        func2(0);
        func3(arr);

    }
    public static int[] func1(String[] arr) {
        for (int i = 1; i < arr.length; i++){
            arr[i] = 0;
        }
        return arr;
    }
    public static int func2(int num){
        int value = 10;
        return  value/num;
    }
    public static String[] func3(String[] arr) {
        for (int i = 0; i <= arr.length ; i++) {
            arr[i]+=" ";
        }
        return arr;
    }
}
