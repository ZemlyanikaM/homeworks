// Задайте одномерный массив, заполненный случайными числами. 
// Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0


int[] arr = new int[8];
FillArray(arr);
PrintArray(arr);
int sum = FindSumOddIndex(arr);
Console.WriteLine($"The sum of odd elemets = {sum}");
void FillArray(int[] arr)
{
    int length = arr.Length;
    for (int i = 0; i < length; i++)
    {
        arr[i] = new Random().Next(-99, 100);
    }
}
void PrintArray(int[] arr)
{
    int len = arr.Length;
    for (int i = 0; i < len; i++)
    {
        Console.Write($"{arr[i]} ");
    }
    Console.WriteLine();
}
int FindSumOddIndex(int[] arr)
{
    int sum = 0;
    for (int i = 1; i < arr.Length; i += 2)
    {
        sum += arr[i];
    }
    return sum;
}