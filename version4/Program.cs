using System;
using System.Collections.Specialized;
using System.Linq.Expressions;
using version4.classes;

namespace version4
{

    internal class Program
    {
        static void Main(string[] args)
        {
            util util = new util();
            menu menu = new menu();
            menutext menutext = new menutext(util, menu);

            var key = Console.ReadKey(false).Key;
            Console.WriteLine(key.ToString());
            Console.ReadKey();


            menutext.addtext("test text 1");
            menutext.addtext("no", "test2");
            menutext.addtext("test text 2");
            menutext.addtext("test text 3");
            menutext.addtext("yes", "runshit");
            while (true)
            {
                menutext.writetext(new List<int> { 1, 2, 3, 4, 5});
            }

        }
        public static void runshit()
        {
            Console.Clear();
            Console.WriteLine("runshit");
            Console.ReadKey();
        }

        public static void test2()
        {
            Console.Clear();
            Console.WriteLine("test 2 /no");
            Console.ReadKey();
        }

    }
} 