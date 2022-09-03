int MaxOf3(int number1, int number2, int number3)
{
    int result = number1;
    if (number2 > result) result = number2;
    if (number3 > result) result = number3;
    return(result);
}

int GetData()
{
    Console.Write("Enter number ");
    return(Convert.ToInt32(Console.ReadLine()));
}

int max = MaxOf3(GetData(), GetData(), GetData());
Console.Write("The maximum is: ");
Console.WriteLine(max);