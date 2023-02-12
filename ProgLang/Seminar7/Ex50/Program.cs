// Задача 50: Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и
// возвращает значение этого элемента или же указание, что такого элемента нет.
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
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
int rows = new Random().Next(3, 6);
int columns = new Random().Next(5, 10);
int[,] arr = new int[rows, columns];
FillMatrix(arr);
int i = InputNumber("Enter the row> ");
int j = InputNumber("Enter the column> ");
if (i < rows && j < columns)
{
    Console.WriteLine($"The element [{i},{j}] of the matrix is: {arr[i, j]}");
}
else
{
    Console.WriteLine($"There's no element [{i},{j}] in the matrix.");
}
PrintMatrix(arr);
