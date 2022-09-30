// Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. 
// Выполнить с помощью рекурсии.
// N = 5 -> "5, 4, 3, 2, 1"
// N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1"
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
string PrintNumRec(int n)
{
    if (n == 0)
    {
        return 0.ToString();
    }
    if (n == 1)
    {
        return 1.ToString();
    }
    return (n + "," + PrintNumRec(n - 1));

}
int n = InputNumber("Enter N: ");
Console.WriteLine(PrintNumRec(n));