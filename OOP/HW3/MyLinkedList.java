package Seminar3.HW3;
import java.util.Iterator;
public class MyLinkedList<E> implements Iterable<E> {
    private int size = 0;
    private ListElement<E> listElement = new ListElement<>();
    private class ListElement<E> {
        private E value;
        private ListElement<E> next;
        private ListElement<E> previous;
        ListElement() {
            this.value = null;
            this.next = null;
            this.previous = null;
        }
        ListElement(E value) {
            this.value = value;
            this.next = null;
            this.previous = (ListElement<E>) getListElement(size);
        }
        void setValue(E value) {
            this.value = value;
        }
        E getValue() {
            return value;
        }
        boolean isNext() {
            return next != null;
        }
        void addValue(E value) {
            if (isNext()) {
                next.addValue(value);
            } else {
                next = new ListElement<>(value);
            }
        }

        @Override
        public String toString() {
            return value.toString();
        }
    }
    private ListElement<E> getListElement(int index) {
        ListElement<E> result;
        if (size == 1) {
            return listElement;
        } else {
            int count = 1;
            result = listElement;
            while (count < index) {
                result = result.next;
                count++;
            }
        }
        return result;
    }

    public void add(E value) {
        if (size == 0) {
            listElement.setValue(value);
            size++;
        } else {
            listElement.addValue(value);
            size++;
        }
    }

    public int size() {
        return size;
    }

    @Override
    public Iterator<E> iterator() {
        return new Iterator<E>() {
            ListElement<E> item = listElement;
            boolean start = true;

            @Override
            public boolean hasNext() {
                if (size == 1 && start) {
                    return true;
                }
                return item.isNext();
            }

            @Override
            public E next() {
                if (start) {
                    start = false;
                } else {
                    item = item.next;
                }
                return item.getValue();
            }
        };
    }

}