using System;
using System.Collections;

namespace CoronaPivot
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args[0].ToUpper() == "CORONA")
            {                
                System.IO.StreamReader srCorona = new System.IO.StreamReader(args[1]);
                System.IO.StreamWriter swCorona = new System.IO.StreamWriter(args[2], false);

                String header = srCorona.ReadLine();

                String[] headers = header.Split(",");

                swCorona.WriteLine("countyFIPS,County Name,State,stateFIPS,Date,New Cases,Running Total");

                while (!srCorona.EndOfStream)
                {
                    int lastRunningTotal = 0;
                    String line = srCorona.ReadLine();

                    String[] lineValues = line.Split(",");

                    CoronaEntry coronaEntry = new CoronaEntry();

                    coronaEntry.CountyFIPS = int.Parse(lineValues[0]);
                    coronaEntry.CountyName = lineValues[1];
                    coronaEntry.State = lineValues[2];
                    coronaEntry.StateFIPS = int.Parse(lineValues[3]);

                    for (int i = 4; i < lineValues.Length; i++)
                    {
                        CoronaDate coronaConfirmedDate = new CoronaDate();
                        coronaConfirmedDate.Date = DateTime.Parse(headers[i]);
                        coronaConfirmedDate.RunningTotal = int.Parse(lineValues[i]);
                        coronaConfirmedDate.DayTotal = coronaConfirmedDate.RunningTotal - lastRunningTotal;

                        lastRunningTotal = coronaConfirmedDate.RunningTotal;

                        coronaEntry.CoronaDates.Add(coronaConfirmedDate);
                    }

                    swCorona.Write(coronaEntry.ToString());
                }

                srCorona.Close();

                swCorona.Flush();
                swCorona.Close();                
            }
        }
    }
}
