using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace version4.classes
{
    internal class menutext
    {
        public util _util { get; set; }
        public menu _menu { get; set; }
        private Dictionary<int, Tuple<string, string>> textdictionary = new Dictionary<int, Tuple<string, string> > { { 0, new Tuple<string, string>("", "-") } };
        private int textcount = 0;
        private int selectedText = 0;
        public List<int> writethistext = new List<int>();
        menutext _menutext { get; set; }
        public menutext(util util, menu menu)
        {
            _util = util;
            _menu = menu;
        }
        public void setmenutexttoself(menutext menutext)
        {
            _menutext = menutext;
        }

        public void addtext(string text, string test)
        {
            textcount++;
            textdictionary.Add(textcount, new Tuple<string, string> (text, test ));
        }
        public void addtext(string text)
        {
            textcount++;
            textdictionary.Add(textcount, new Tuple<string, string>(text, "-"));
        }

        public void removealltext()
        {
            textdictionary = new Dictionary<int, Tuple<string, string>> { { 0, new Tuple<string, string>("", "-") } };
        }

        public void setshowntext(List<int> newlist)
        {
            writethistext = newlist;
            writethistext.Insert(0, 0);
        }


        public void writetext()
        {
            selectedText = Math.Clamp(selectedText, writethistext[0], writethistext[writethistext.Count - 1]);
            Console.Clear();
            foreach (int writetextkey in writethistext)
            {
                if (writetextkey == selectedText )
                {
                    _menutext.writeformatedtext(textdictionary[writetextkey].Item1);
                }
                else { _menutext.writeunselectedtext(textdictionary[writetextkey].Item1); }
            }
            int input = _menu.detect_direction(_util);
            object[] parm = { _util, _menu, _menutext };
            if (input == 2) { typeof(version4.Program).GetMethod(textdictionary[selectedText].Item2)?.Invoke(null, parm); }

            else
            {
                try
                {
                    if (input == 1 && selectedText == writethistext[writethistext.Count-1])
                    {
                        selectedText = 0;
                    }
                    else if (input == -1 && selectedText == writethistext[0])
                    {
                        selectedText = writethistext[writethistext.Count - 1];
                    }
                    if (input == 1)
                    {
                        selectedText++;
                        while (textdictionary[selectedText].Item2 == "-")
                        {
                            {
                                if (selectedText == writethistext[writethistext.Count - 1])
                                {
                                    selectedText = writethistext[0];
                                }
                                else
                                {
                                    selectedText++;
                                }
                            }
                        }
                    }
                    else
                    {
                        selectedText--;
                        while (textdictionary[selectedText].Item2 == "-")
                        {
                            if (selectedText == 0)
                            {
                                selectedText = writethistext[writethistext.Count - 1];
                            }
                            else
                            {
                                selectedText--;
                            }
                        }
                    }
                }
                catch
                {
                    return;
                }
                selectedText = Math.Clamp(selectedText, writethistext[0], writethistext[writethistext.Count - 1]);
            }
        }
    
        public void writeformatedtext(string text)
        {
            List<char> splittext = text.ToList();
            if (string.Join("", splittext).Contains("["))
            {
                foreach (char c in splittext)
                {
                    if (c == '[')
                    {
                        Console.BackgroundColor = ConsoleColor.White;
                        Console.ForegroundColor = ConsoleColor.Black;
                    }
                    else if (c ==  ']') { Console.ResetColor(); }
                    else
                    { Console.Write(c); }
                }
                Console.WriteLine();
            }
            else { writelineselectedtext(text); }
        }

        public void writeunselectedtext(string text)
        {
            List<char> splittext = text.ToList();
            foreach (char c in splittext)
            {
                if (c == '[')
                {
                    continue;
                }
                else if (c == ']') { continue; }
                else { Console.Write(c); }
            }
            Console.WriteLine();
        }
    
    public void writelineselectedtext(string text)
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.WriteLine(text);
            Console.ResetColor();
        }
    }
}
