package sem2.hw;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 45, 76, 0, 76, 546, -12, -7};
        sort(arr);
        System.out.println(Arrays.toString(arr));

    }

    public static void sort(int[] arr) {
        for (int i = arr.length / 2 - 1; i >= 0; i--)
            heapyfy(arr, arr.length, i);
        for (int i = arr.length - 1; i >= 0; i--) {
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
            heapyfy(arr, i, 0);
        }

    }

    private static void heapyfy(int[] arr, int hSize, int rootIndex) {
        int max = rootIndex;
        int leftCh = 2 * rootIndex + 1;
        int rightCh = 2 * rootIndex + 2;
        if (leftCh < hSize && arr[leftCh] > arr[max])
            max = leftCh;
        if (rightCh < hSize && arr[rightCh] > arr[max])
            max = rightCh;
        if (max != rootIndex) {
            int tmp = arr[rootIndex];
            arr[rootIndex] = arr[max];
            arr[max] = tmp;
            heapyfy(arr, hSize, max);
        }
    }
}
