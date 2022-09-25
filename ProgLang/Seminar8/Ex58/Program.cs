// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18
void FillMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            arr[i, j] = new Random().Next(1, 4);
        }

    }
}
void PrintMatrix(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            Console.Write("{0,2} ", arr[i, j]);
        }
        Console.WriteLine();
    }
}
int[,] GetMatrixMultiplication(int[,] matrixA, int[,] matrixB)
{
    int[,] matrixC = new int[matrixA.GetLength(0), matrixB.GetLength(1)];
    for (int k = 0; k < matrixA.GetLength(0); k++)
    {
        for (int i = 0; i < matrixB.GetLength(1); i++)
        {
            for (int j = 0; j < matrixB.GetLength(0); j++)
            {
                matrixC[k, i] += matrixA[k, j] * matrixB[j, i];
            }
        }
    }
    return matrixC;
}

int rows = new Random().Next(2, 6);
int columns = new Random().Next(2, 6);
int[,] matrixA = new int[rows, columns];
int[,] matrixB = new int[columns, rows];
FillMatrix(matrixA);
FillMatrix(matrixB);
Console.WriteLine("The martix A:");
PrintMatrix(matrixA);
Console.WriteLine("The martix B:");
PrintMatrix(matrixB);
Console.WriteLine("The martix C=A*B:");
PrintMatrix(GetMatrixMultiplication(matrixA, matrixB));
