// Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07
void PrintMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            Console.Write("{0,2} ", arr[i, j]);
        }
        Console.WriteLine();
    }
}
int size = new Random().Next(2, 6);
int[,] arr = new int[size, size];
int value = 0;
int layer = 0;
int i, j = 0;
while (value < arr.Length)
{
    for (i = layer; i < size; i++)
    {
        arr[j, i] = value;
        value++;
    }
    j = size - 1;
    for (i = layer + 1; i < size; i++)
    {
        arr[i, j] = value;
        value++;
    }
    for (i = size - 2; i >= layer; i--)
    {
        arr[j, i] = value;
        value++;
    }
    j = layer;
    for (i = size - 2; i > layer; i--)
    {
        arr[i, j] = value;
        value++;
    }
    size--;
    layer++;
    j = layer;
}
PrintMatrix(arr);