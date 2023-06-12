package sem1.hw;

public class task2 {
    public static void main(String[] args) {
    }
    public static int sum2d(String[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            //Массив может быть пустым - NullPointerException
            for (int j = 0; j < 2; j++) {
                //Магическая цифра - может прийти массив меньшей размерности - IndexOutOfBoundsException
                int val = Integer.parseInt(arr[i][j]);
                //может прийти символ не подлежащий парсингу - NumberFormatException
                sum += val;
            }
        }
        return sum;
    }
}
