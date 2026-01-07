using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Excer___02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num = 28;
            int rem;
            rem = num % 2;
            if (rem == 0)
            {
                Console.WriteLine(num,"is even");
            }
            else {
                Console.WriteLine(num,"is odd");
        }
            Console.ReadLine();
    }
}
