// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
// [3 7 22 2 78] -> 76

double[] arr = new double[8];
FillArray(arr);
PrintArray(arr);
double diff = FindMaxMinDiff(arr);
Console.WriteLine($" maximum - minimum  = {diff}");
void FillArray(double[] arr)
{
    int length = arr.Length;
    for (int i = 0; i < length; i++)
    {
        arr[i] = new Random().NextDouble() * 10;
    }
}
void PrintArray(double[] arr)
{
    int len = arr.Length;
    for (int i = 0; i < len; i++)
    {
        Console.Write($"{arr[i]} ");
    }
    Console.WriteLine();
}
double FindMaxMinDiff(double[] arr)
{
    double max = arr[0];
    double min = arr[0];
    for (int i = 1; i < arr.Length; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
        if (min > arr[i])
        {
            min = arr[i];
        }
    }
    double diff = max - min;
    Console.WriteLine($"The maximum = {max}");
    Console.WriteLine($"The minimum = {min}");
    return diff;
}