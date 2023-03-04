package Seminar3.HW3;

public class Main {
    public static void main(String[] args) {
        MyLinkedList<String> hello = new MyLinkedList<>();
        hello.add("Hello");
        hello.add(",");
        hello.add(" ");
        hello.add("World");
        hello.add("!");

        for (String item:hello) {
            System.out.print(item);
        }
        System.out.println();
        System.out.printf("Size: %d", hello.size());
        System.out.println();
        MyLinkedList<Integer> nums = new MyLinkedList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);
        nums.add(6);
        nums.add(7);

        for (Integer item:nums) {
            System.out.println(item);
        }
        System.out.printf("Size: %d", nums.size());

    }
}