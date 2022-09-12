// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12


int InputNumber()
{
    Console.Write("Enter a number >");
    int num = Convert.ToInt32(Console.ReadLine());
    return num;
}

int GetDigitSum(int num)
{
    int sum = 0;
    while (num > 0)
    {
        sum += num % 10;
        num = num / 10;
    }
    return sum;
}
int number = InputNumber();
int sum = GetDigitSum(number);
Console.WriteLine($"The sum of digits of the number {number} is: {sum}");