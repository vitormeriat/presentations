using System;

namespace GlobalAiBootcamp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World CNTK!!!\n\n");

            Utils.PrintCNTKVersion();

            Utils.Normalization();
             
            Console.ReadLine();
        }        
    }
}
