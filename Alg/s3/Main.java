package sem3.hw;

public class Main {
    public static void main(String[] args) {
        DoubleLinkedList list = new DoubleLinkedList();
        for (int i = 0; i < 10; i++) {
            list.addNode(i);
        }
        list.reverseList();
        list.printList();
    }
}
