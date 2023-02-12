// Задача 54: Задайте двумерный массив. 
// Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 7 4 2 1
// 9 5 3 2
// 8 4 4 2


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
void SortMatrix(int[,] arr)
{
    for (int k = 0; k < arr.Length - 1; k++)
    {
        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1) - 1; j++)
            {
                if (arr[i, j] < arr[i, j + 1])
                {
                    int tmp = arr[i, j];
                    arr[i, j] = arr[i, j + 1];
                    arr[i, j + 1] = tmp;
                }
            }
        }
    }
}
int rows = new Random().Next(3, 8);
int columns = new Random().Next(3, 8);
int[,] arr = new int[rows, columns];
FillMatrix(arr);
PrintMatrix(arr);
Console.WriteLine();
SortMatrix(arr);
PrintMatrix(arr);