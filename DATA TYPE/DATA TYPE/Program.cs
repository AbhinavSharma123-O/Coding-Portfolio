using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DATA_TYPE
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int x = 32, y = 123, z = 12;
            int age = 12;
            long bigNum = 90000000000L;
            Console.WriteLine(age);
            Console.WriteLine(bigNum);
            Console.WriteLine(int.MaxValue);
            Console.WriteLine(int.MinValue);
            Console.WriteLine(long.MaxValue);
            Console.WriteLine(long.MinValue);
            double negative = -21.6d;
            Console.WriteLine(negative);
            Console.WriteLine(double.MaxValue);
            Console.WriteLine(double.MinValue);
            float precision = 5000.00001F;
            Console.WriteLine(precision);
            Console.WriteLine(float.MaxValue);
            Console.WriteLine(float.MinValue);

            Console.ReadLine();
        }
    }
}
