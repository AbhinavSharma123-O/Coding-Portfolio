using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Const
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const int vat = 20;
           
            int balance = 1000;
            
            Console.WriteLine(balance * (vat / 10));
            Console.WriteLine(vat);
            Console.ReadLine();
        }
    }
}
