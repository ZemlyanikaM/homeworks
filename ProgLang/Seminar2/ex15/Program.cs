//Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
//является ли этот день выходным.
//6 -> да
//7 -> да
//1 -> нет
Console.Write("What is a day (1..7) today? ");
int day = Convert.ToInt32(Console.ReadLine());
bool CheckTheDayOff(int num)
{
    return  num > 5;
}
if (day < 1 || day > 7)
{
    Console.WriteLine("The day is out of range (1..7), enter a valid day");    
}
else if (CheckTheDayOff(day) == true)
{
    Console.WriteLine($"The {day} day is a day off.");
}
else 
{
    Console.WriteLine($"The {day} day is not a day off.");
}
