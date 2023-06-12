package sem1.hw;

import java.util.Arrays;
public class task3 {
    public static void main(String[] args) {
        int[] arr1 = {34, 6, 17, 9};
        int[] arr2 = {21, 1, 9, 2};
        try {
            int[] diff = diffArr(arr1, arr2);
            System.out.println(Arrays.toString(diff));
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }

    public static int[] diffArr(int[] arr1, int[] arr2) throws IllegalArgumentException {
        if (arr1.length != arr2.length) {
            throw new IllegalArgumentException("Arrays have different lengths");
        }
        int[] diff = new int[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            diff[i] = arr1[i] - arr2[i];
        }
        return diff;
    }
}
