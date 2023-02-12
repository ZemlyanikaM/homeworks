//  Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
//  3, 5 -> 243 (3⁵)
// 2, 4 -> 16


int InputNumber(string name)
{
    Console.Write($"Enter a number {name} >");
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
int exponentiate(int a, int b)
{
    int exp = 1;
    for (int i = 0; i < b; i++)
    {
        exp *= a;
    }
    return exp;
}
int numA = InputNumber("A");
int numB = InputNumber("B");
int result = exponentiate(numA, numB);
Console.WriteLine($"{numA} to the power {numB} = {result}");
