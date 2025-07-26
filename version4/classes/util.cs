using System;
using System.Collections.Specialized;
using System.Numerics;


public class util
{
    public void writelineselectedtext(string text)
    {
        Console.BackgroundColor = ConsoleColor.White;
        Console.ForegroundColor = ConsoleColor.Black;
        Console.WriteLine(text);
        Console.ResetColor();
    }

    //second variable is unused and only used to define the expected return type
    public util()
    {
        
    }
    public string askquestion(string question)
    {
        while (true)
        {
            Console.WriteLine(question);
            var awnser = Console.ReadLine();
            if (awnser != null)
            {
                return awnser;
            }
        }
    }

    public int askquestion(string question, int temp)
    {
        while (true)
        {
            Console.WriteLine(question);
            Console.WriteLine("Please awnser with a whole number");
            try
            {
                int awnser = int.Parse(Console.ReadLine());
                return awnser;
            }
            catch
            {
                Console.WriteLine("invalid awnser press any key to continue");
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
    public bool askquestion(string question, Dictionary<string, bool> expectedboolawnsers) //expected bool awnsers is give as a dictonary where the key is the expected anwser and the value is the returned bool
    {

        while (true)
        {
            Console.WriteLine(question);
            Console.WriteLine("for all possible awnsers please type 'awnsers'");
            try
            {
                string awnser = Console.ReadLine();
                if (awnser == "awnsers")
                {
                    string toprint = "";
                    foreach (string key in expectedboolawnsers.Keys)
                    {
                        toprint += key;
                        toprint += ", ";
                    }
                    Console.WriteLine(toprint);
                    Console.WriteLine("press any key to continue");
                    Console.ReadKey();
                    Console.Clear();
                }
                else if (expectedboolawnsers.ContainsKey(awnser))
                {
                    return expectedboolawnsers[awnser];
                }
                else
                {
                    Console.WriteLine("invalid awnser press any key to continue");
                    Console.ReadKey();
                    Console.Clear();
                }
            }
            catch
            {
                Console.WriteLine("invalid awnser press any key to continue");
                Console.ReadKey();
                Console.Clear();
            }
        }

    }

    public double askquestion(string question, double temp)
    {
        while (true)
        {
            Console.WriteLine(question);
            Console.WriteLine("please awnser with a number");
            try
            {
                double awnser = double.Parse(Console.ReadLine());
                return awnser;
            }
            catch
            {
                Console.WriteLine("invalid awnser press any key to continue");
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
}

public class menu
{
    public menu()
    {
        
    }

    public Tuple<int, int> detect_direction(util util)
    {
        Tuple<int, int> direction = new Tuple<int, int>(0, 0);
        var key = Console.ReadKey(false).Key;
        
        switch (key.ToString())
        {
            case "UpArrow":
                direction = new Tuple<int, int>(1, 0);
                break;

            case "DownArrow":
                direction = new Tuple<int, int>(-1, 0);
                break;

            case "LeftArrow":
                direction = new Tuple<int, int>(0, 1);
                break;

            case "RightArrow":
                direction = new Tuple<int, int>(0, -1);
                break;
            default:
                break;
        }
        Console.Clear();
        Console.WriteLine(direction.ToString());
        util.writelineselectedtext("test text");
        return direction;
    }

}
