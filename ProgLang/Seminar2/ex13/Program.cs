// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей 
//цифры нет.
//645 -> 5
//78 -> третьей цифры нет
//32679 -> 6

//Console.Write("Enter a number> ");
//string num = Console.ReadLine();
//Console.WriteLine(num[2]);

Console.Write("Enter a number> ");
int num = Convert.ToInt32(Console.ReadLine());
int GetDig(int number)
{
    while (number > 999)
    {
        number = number / 10;
    }
    number = number % 10;
    return(number);
}
if (num < 100)
{
    Console.WriteLine($"There is no 3th digit in {num}");
}
else
{
    int dig = GetDig(num) ;
    Console.WriteLine($"The 3th digit of {num} is {dig}");
} 
