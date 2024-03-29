﻿// Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
//Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
// Массив размером 2 x 2 x 2
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)

void FillNPrintCube(int[,,] cube)
{
    int value = 10;
    for (int i = 0; i < cube.GetLength(0); i++)
    {
        for (int j = 0; j < cube.GetLength(1); j++)
        {
            for (int k = 0; k < cube.GetLength(2); k++)
            {
                cube[i, j, k] = value;
                value++;
                Console.Write($"{cube[i, j, k]} ({i},{j},{k})   ");
            }
            System.Console.WriteLine();
        }
    }
}
int cubeSize = new Random().Next(2, 5);
int[,,] cube = new int[cubeSize, cubeSize, cubeSize];
FillNPrintCube(cube);