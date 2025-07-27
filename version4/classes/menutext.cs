using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace version4.classes
{
    internal class menutext
    {
        public util _util { get; set; }
        public menu _menu { get; set; }
        private Dictionary<int, Tuple<string, string>> textdictionary = new Dictionary<int, Tuple<string, string> > { { 0, new Tuple<string, string>("don't use 0 i geuss", "-") } };
        private int textcount = 0;
        private int selectedText = 0;
        public menutext(util util, menu menu)
        {
            _util = util;
            _menu = menu;
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

        public void writetext(List<int> writethistext)
        {
            selectedText = Math.Clamp(selectedText, writethistext[0], writethistext[writethistext.Count - 1]);
            Console.Clear();
            foreach (int writetextkey in writethistext)
            {
                if (writetextkey == selectedText )
                {
                    _util.writelineselectedtext(textdictionary[writetextkey].Item1);
                }
                else { Console.WriteLine(textdictionary[writetextkey].Item1); }
            }
            int input = _menu.detect_direction(_util);
            if (input == 2) { typeof(version4.Program).GetMethod(textdictionary[selectedText].Item2)?.Invoke(null, null); }

            else
            {
                selectedText += input;
                try
                {
                    while (textdictionary[selectedText].Item2 == "-") { selectedText++; }
                }
                catch
                {
                    return;
                }
                selectedText = Math.Clamp(selectedText, writethistext[0], writethistext[writethistext.Count - 1]);
            }
        }
    }
}
