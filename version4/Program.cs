using System;
using System.Collections.Specialized;

namespace version4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            util util = new util();
            menu menu = new menu();

            while (true)
            {
                menu.detect_direction(util);
            }

        }
    }
}
