Console.Clear();
Console.Write("Enter a number N> ");
int numberN = Convert.ToInt32(Console.ReadLine());
if (numberN == 1)
{
    Console.Write("There're no any even numbers from 1 to 1");
}
else if (numberN > 1)
{
    Console.Write("Even numbers from 1 to ");
    Console.WriteLine(numberN);
    int count = 2;
    while (count <= numberN)
    {
        Console.Write(count);
        count = count + 2;
        Console.Write(" ");
    }
    Console.WriteLine("");   
}
else
{
    Console.Write("Even numbers from 1 to ");
    Console.WriteLine(numberN);
    int count = 0;
    while (count >= numberN)
    {
        Console.Write(count);
        count = count - 2;
        Console.Write(" ");
    }
    Console.WriteLine("");   
}