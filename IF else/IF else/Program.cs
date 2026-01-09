using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IF_else
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your age:- ");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Your age is " + age);
            if (age > 18 && age<90)
            {
                Console.WriteLine("ID is posible,cause age is " + age);
            }
            else if (age == 18)
            {
                Console.WriteLine("Check again,cause age is " + age);
            }
            else if (age < 0 || age>1000)
            {
                Console.WriteLine("Invalid age");
            }
            else
            {
                Console.WriteLine("ID is not possible,cause age is " + age);
            }
            Console.ReadLine();
        }
    }
}
