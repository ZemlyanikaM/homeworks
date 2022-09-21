// Задача 47: Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.

void FillMatrix(double[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            arr[i, j] = new Random().NextDouble() * 10;
        }
    }
}
void PrintMatrix(double[,] arr)
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
int rows = new Random().Next(2, 6);
int columns = new Random().Next(2, 6);
double[,] arr = new double[rows, columns];
FillMatrix(arr);
PrintMatrix(arr);
