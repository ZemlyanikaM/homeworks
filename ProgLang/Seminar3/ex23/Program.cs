// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125
Console.Write("Enter N: ");
int N = Convert.ToInt32(Console.ReadLine());
void Cubes(int num)
{
    int count = 1;
    while (count <= num)
    {
        Console.WriteLine((int)Math.Pow(count, 3));
        count++;
    }
}
Cubes(N);
