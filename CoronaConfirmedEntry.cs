using System;
using System.Collections.Generic;
using System.Text;

public class CoronaEntry {
    public int CountyFIPS;
    public String CountyName;
    public String State;
    public int StateFIPS;

    public List<CoronaDate> CoronaDates  = new List<CoronaDate>();

    public CoronaEntry() {
        this.CountyFIPS = 0;
        this.CountyName = "";
        this.State = "";
        this.StateFIPS = 0;
    }

    public override String ToString() {
        StringBuilder sb = new StringBuilder();        

        foreach(CoronaDate cd in this.CoronaDates) {
            sb.Append(this.CountyFIPS);
            sb.Append(",");
            sb.Append(this.CountyName);
            sb.Append(",");
            sb.Append(this.State);
            sb.Append(",");
            sb.Append(this.StateFIPS);
            sb.Append(",");
            sb.Append(cd.Date);            
            sb.Append(",");
            sb.Append(cd.DayTotal);
            sb.Append(",");
            sb.Append(cd.RunningTotal);
            sb.AppendLine();
        }

        return sb.ToString();
    }
}