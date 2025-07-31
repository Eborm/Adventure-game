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
            menutext.setmenutexttoself(menutext);

            var key = Console.ReadKey(false).Key;
            Console.WriteLine(key.ToString());
            Console.ReadKey();


            menutext.addtext("test text 1");
            menutext.addtext("test text 2");
            menutext.addtext("no", "test2");
            menutext.addtext("test text 3");
            menutext.addtext("remove text [yes]", "runshit");
            menutext.addtext("removed all text");
            menutext.setshowntext(new List<int> { 1, 2, 3, 4, 5 });
            while (true)
            {
                menutext.writetext();
            }

        }
        public static void runshit(util _util, menu _menu, menutext _menutext)
        {
            Console.Clear();
            _menutext.setshowntext(new List<int> { 6});
        }

        public static void test2(util _util, menu _menu, menutext _menutext)
        {
            Console.Clear();
            Console.WriteLine("test 2 /no");
            Console.ReadKey();
        }

    }
} 