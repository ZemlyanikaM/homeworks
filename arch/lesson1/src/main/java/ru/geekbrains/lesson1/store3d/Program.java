package ru.geekbrains.lesson1.store3d;

import ru.geekbrains.lesson1.store3d.inmemorymodel.CustomService1;
import ru.geekbrains.lesson1.store3d.inmemorymodel.CustomService2;
import ru.geekbrains.lesson1.store3d.inmemorymodel.CustomService3;
import ru.geekbrains.lesson1.store3d.inmemorymodel.ModelStore;

public class Program {

    public static void main(String[] args) throws Exception {

        CustomService1 observer1 = new CustomService1();
        CustomService2 observer2 = new CustomService2();
        CustomService3 observer3 = new CustomService3();


        ModelStore modelStore = new ModelStore();
        modelStore.registerModelChanger(observer1);
        modelStore.registerModelChanger(observer2);
        modelStore.registerModelChanger(observer3);


    }

}
