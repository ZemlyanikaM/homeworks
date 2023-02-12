// Задача 56: Задайте прямоугольный двумерный массив. 
// Напишите программу, которая будет находить строку с наименьшей суммой элементов.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7
// Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 
// 1 строка
void FillMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            arr[i, j] = new Random().Next(0, 10);
        }

    }
}
void PrintMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            Console.Write($" {arr[i, j]} ");
        }
        Console.WriteLine();
    }
}
int FindMinsSumRow(int[,] arr)
{
    int currentSum = 0;
    int sum = 99999999;
    int minSumRow = 0;
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            currentSum += arr[i, j];
        }
        if (currentSum < sum)
        {
            sum = currentSum;
            minSumRow = i;
        }
        currentSum = 0;
    }
    return minSumRow;
}

int rows = new Random().Next(5, 8);
int columns = new Random().Next(3, 5);
int[,] arr = new int[rows, columns];
FillMatrix(arr);
PrintMatrix(arr);
int minSumRow = FindMinsSumRow(arr);
Console.WriteLine($"The row with the minimum sum is: {minSumRow}");