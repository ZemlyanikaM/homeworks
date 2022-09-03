//  Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру 
//  этого числа. 
//456 -> 5
//782 -> 8
//918 -> 1
Console.Write("Enter a number (100-999)> ");
int num = Convert.ToInt32(Console.ReadLine());

void ShowMiddleDig(int number)
{
    number = number / 10 % 10;
    Console.WriteLine($"The middle digit is: {number}");
}
if (num < 100 || num > 999)
{
    Console.WriteLine($"The number {num} is out of range (100 - 999), enter a valid number");
}
else
{
    ShowMiddleDig(num);
}
