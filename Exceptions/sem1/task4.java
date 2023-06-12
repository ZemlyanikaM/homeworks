package sem1.hw;

import java.util.Arrays;

public class task4 {
    public static void main(String[] args) {
        int[] arr1 = {34, 6, 17, 9};
        int[] arr2 = {21, 1, 0, 2};
        try {
            int[] divided = divArr(arr1, arr2);
            System.out.println(Arrays.toString(divided));
        } catch (RuntimeException e) {
            System.err.println(e.getMessage());
        }
    }

    public static int[] divArr(int[] arr1, int[] arr2) throws RuntimeException {
        if (arr1.length != arr2.length) {
            throw new RuntimeException("Arrays have different lengths");
        }
        int[] divided = new int[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            if (arr2[i] == 0){
                throw new RuntimeException("Dividing by 0");
            }
            else {
                divided[i] = arr1[i] / arr2[i];
            }
        }
        return divided;
    }
}
