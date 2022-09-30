// Задача 66: Задайте значения M и N. 
//Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30
int SumNumsRec(int start, int end)
{
    if (start == end)
    {
        return start;
    }
    if (start < end)
    {
        return (start + SumNumsRec(start + 1, end));
    }
    else
    {
        return (start + SumNumsRec(start - 1, end));
    }

}
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
int m = InputNumber("Enter M: ");
int n = InputNumber("Enter N: ");
Console.WriteLine(SumNumsRec(m, n));
