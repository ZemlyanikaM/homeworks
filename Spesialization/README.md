# Задача.
### Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры,  либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами. 


* string[] array - входящий массив строк, задан в коде.
*  string[] result = new string[CountSmallWords(array)];  - результируйщий массив, содержащий искомые строки. Размер вычесляется с помощью ниже описанного метода.
* int CountSmallWords(string[] array) - метод вычисляет количество строк длина которых <= 3 в заданном массиве строк array. Возвращает целочисленное значение, количество строк соответствующих условию. В случае возврата 0, в консоль выводит сообщение об отсутсвии искомых строк в массиве.

* void GetSmallWords(string[] array, string[] result) - метод заполняет результирующий массив result элементами массива array, удовлетворяющими поставленному условию.

* void PrintArray(string[] result) - метод выводящий в консоль содержимое массива. Принимает выводимый массив.