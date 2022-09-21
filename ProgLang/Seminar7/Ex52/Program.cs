// Задача 52: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

void FillMatrix(double[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            arr[i, j] = (double)new Random().Next(0, 10);
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
void ShowColumnsAverage(double[,] arr)
{

    for (int i = 0; i < arr.GetLength(1); i++)
    {
        double sum = 0;
        double average = 0;
        for (int j = 0; j < arr.GetLength(0); j++)
        {
            sum += arr[j, i];
        }
        average = sum / arr.GetLength(0);
        Console.WriteLine($"The average of column {i} = {average}");
    }
}
int rows = new Random().Next(3, 6);
int columns = new Random().Next(5, 10);
double[,] arr = new double[rows, columns];
FillMatrix(arr);
ShowColumnsAverage(arr);
PrintMatrix(arr);
