using System.Diagnostics.Metrics;

namespace Singleton.Core;

public class GlobalCounter
{
    public static GlobalCounter? Instance;
    public Dictionary<string, int> Counters = new();


    private GlobalCounter() { }

    public static GlobalCounter GetInstance()
    {
        Instance ??= new GlobalCounter();
        return Instance;
    }

    public static void ResetInstance() { }

    public int Increment(string counterName)
    {
        return 0;
    }
    public int GetValue(string counterName)
    {
        return 0;
    }
    public int Decrement(string counterName)
    {
        return 0;
    }
    public int Reset(string counterName = "")
    {
        return 0;
    }
    public Dictionary<string, int> ListCounters()
    {
        return Counters;
    }

}
