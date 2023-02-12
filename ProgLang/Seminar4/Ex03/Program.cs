// Напишите программу, которая выводит массив из 8 элементов, заполненный случайными числами.
// Оформите заполнение массива и вывод в виде функции (пригодится в следующих задачах)

int[] arr = new int[8];
int[] FillArray(int[] nums)
{
    int length = nums.Length;
    for (int i = 0; i < length; i++)
    {
        nums[i] = new Random().Next(-99, 100);
    }

    return nums;
}
void PrintArray(int[] pr_nums)
{
    int len = pr_nums.Length;
    for (int i = 0; i < len; i++)
    {
        Console.Write($"{pr_nums[i]} ");
    }
    Console.WriteLine();
}

PrintArray(FillArray(arr));