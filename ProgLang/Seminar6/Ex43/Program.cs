// Задача 43. Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями
// y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
// b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
double b1 = InputNumber("Enter b1 > ");
double k1 = InputNumber("Enter k1 > ");
double b2 = InputNumber("Enter b2 > ");
double k2 = InputNumber("Enter k2 > ");
double x = (b2 - b1) / (k1 - k2);
double y = k1 * x + b1;
Console.WriteLine($"The interseption point is: ({x} , {y})");

