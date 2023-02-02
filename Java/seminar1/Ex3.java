//Дан массив nums = [3,2,2,3] и число val = 3.
//Если в массиве есть числа, равные заданному, нужно перенести эти элементы в конец массива.
//Таким образом, первые несколько (или все) элементов массива должны быть отличны от заданного, а остальные - равны ему.
package seminar1;
import java.util.Arrays;
import java.util.Random;
public class Ex3 {
    public static void main(String[] args) {
        Random rnd = new Random();
        int sortValue = rnd.nextInt(5);
        System.out.printf("sortValue = " + sortValue + '\n');
        System.out.printf("SortedArray = " + Arrays.toString(sortArray(createArray(), sortValue)));
    }
    private static int[] createArray(){
        Random rnd = new Random();
        int length = rnd.nextInt(20);
        int[] col = new int[length];
        for (int i = 0; i < length; i++) {
            col[i] = rnd.nextInt(5);
        }
        System.out.printf("Base array: " + Arrays.toString(col) +"\n");
        return col;
    }
    private static int[] sortArray(int[] col, int sortValue){
        int tmp;
        int l = 0;
        int r = col.length-1;
        while(r>l){
            if (col[l] == sortValue && col[r] != sortValue) {
                tmp = col[r];
                col[r] = col[l];
                col[l]=tmp;
                l++;
                r--;
        } else if (col[l] == sortValue && col[r] == sortValue) {
                r--;
            } else {
                l++;
            }
        }
        return col;
    }

}
