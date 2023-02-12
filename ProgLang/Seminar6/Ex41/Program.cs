// Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3
int InputNumber(string msg)
{
    Console.Write(msg);
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}
int M = InputNumber("How many numbers do you want to enter? ");
int count = 0;
for (int i = 0; i < M; i++)
{
    if( InputNumber($"Enter the number {i + 1} > ") > 0) 
    {
        count++;
    }
}
Console.WriteLine($"Numbers greater than 0: {count}");