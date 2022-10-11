// Написать программу, которая из имеющегося массива строк формирует массив из строк, 
// длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры,
// либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
// лучше обойтись исключительно массивами.

string[] array = { "apple", "dog", "line", "pot", "i", "go", "123", "once" };
string[] result = new string[CountSmallWords(array)];
GetSmallWords(array);
PrintArray(result);

int CountSmallWords(string[] array)
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= 3)
        {
            count++;
        }
    }
    if (count==0)
    {
        Console.WriteLine("There're no any strings in the array less then 4 chars long.");
    }
    return count;
}
