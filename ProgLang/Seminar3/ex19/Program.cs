// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 23432 -> да
// 12821 -> да
Console.Write("Enter a number: ");
string num = Console.ReadLine();
void CheckPalindrom(string number)
{
    int length = number.Length;
    int count  = 0;
    while(count < length / 2) 
    {
         if(number[count] == number[length - count - 1])
        {
            count++;
            if (count==length/2)
            {
                Console.WriteLine($"The {number} is a polindrome ");
            }    
        }
        else
        {
            Console.WriteLine($"The {number} is not a polindrome ");
            break;
        }    
    }    
}
CheckPalindrom(num);
