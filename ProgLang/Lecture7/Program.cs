int n = 20;
double[] arr = new double[n];
arr[0] = 1;
arr[1] = 1;
decimal fRec = 0;
decimal fRecM = 0;

Console.WriteLine(Fibonachi(n));
Console.WriteLine(fRec);
Console.WriteLine();
Console.WriteLine(FibonachiMemRec(n, arr));
Console.WriteLine(fRecM);

double Fibonachi(int n)
{
    fRec++;
    if (n == 1 || n == 2) return 1;
    else return Fibonachi(n - 1) + Fibonachi(n - 2);
}
double FibonachiMemRec(int n, double[] arr)
{
    fRecM++;
    if (n == 0) return 0;
    if (n == 1 || n == 2) return 1;
    if (arr[n - 3] == 0)
    {
        arr[n - 3] = FibonachiMemRec(n - 2, arr);
    }
    if (arr[n - 2] == 0)
    {
        arr[n - 2] = FibonachiMemRec(n - 1, arr);
    }
    arr[n - 1] = arr[n - 3] + arr[n - 2];
    return arr[n - 1];
}
