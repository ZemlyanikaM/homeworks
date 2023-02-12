﻿// Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 9
// m = 3, n = 2 -> A(m,n) = 29
int GetAkkerman(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    if (m > 0 && n == 0)
    {
        return GetAkkerman(m - 1, 1);
    }
    if (m > 0 && n > 0)
    {
        return GetAkkerman(m - 1, GetAkkerman(m, n - 1));
    }
    return GetAkkerman(m, n);

}
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
int m = InputNumber("Enter M: ");
int n = InputNumber("Enter N: ");
Console.WriteLine(GetAkkerman(m, n));
