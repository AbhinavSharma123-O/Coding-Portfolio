using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace If_else_se_math_game
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the first num:- ");
            int num1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter the sec num");
            int num2 = Convert.ToInt32(Console.ReadLine());
            int Asum = num1 + num2;
            int Amul = num1 * num2;
            Console.Write("Enter the Sum:- ");
            int sum = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter the mul:- ");
            int mul = Convert.ToInt32(Console.ReadLine());
            if (sum == Asum && mul == Amul)
            {
                Console.WriteLine("Both are correct");
            }
            else if (sum == Asum)
            {
                Console.WriteLine("Your Addition is correct but Multi is worng........The Correct multi is " + Amul);
            }
            else if (mul == Amul)
            {
                Console.WriteLine("Your muti is correct but add is worng.......The correct add is " + Asum);

            }
            else
            {
                Console.WriteLine("Both are worng......Add= " + Asum + " and multi= " + Amul);
            }

            Console.ReadLine();
        }
    }
}
   

