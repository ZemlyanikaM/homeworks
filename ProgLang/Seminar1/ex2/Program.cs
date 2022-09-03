Console.Clear();
Console.Write("Enter number A>");
int numberA = Convert.ToInt32(Console.ReadLine());
Console.Write("Enter number B>");
int numberB = Convert.ToInt32(Console.ReadLine());
if (numberA > numberB)
{
    Console.Write("The bigger is: ");
    Console.WriteLine(numberA);
    Console.Write("The lesseer is: ");
    Console.WriteLine(numberB);
}
else if (numberA == numberB)
{
    Console.WriteLine("Numbers are equal ");
}
else
{
    Console.Write("The bigger is: ");
    Console.WriteLine(numberB);
    Console.Write("The lesser is: ");
    Console.WriteLine(numberA);
}