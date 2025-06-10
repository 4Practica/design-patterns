namespace Singleton.Core;

public class GlobalCounter
{
    public static GlobalCounter? Instance;
    private Dictionary<string, int> Counters = new();


    private GlobalCounter() { }

    public static GlobalCounter GetInstance()
    {
        Instance ??= new GlobalCounter();
        return Instance;
    }

    public static void ResetInstance()
    {
        Instance = null;
    }

    public int GetValue(string counterName)
    {
        return Counters.TryGetValue(counterName, out int value) ? value : 0;
    }

    public void InitializeCounter(string counterName)
    {
        int value = GetValue(counterName);
        if (value == 0)
            Counters.Add(counterName, 0);
    }

    public void Increment(string counterName)
    {
        InitializeCounter(counterName);
        Counters[counterName]++;
    }

    public void Decrement(string counterName)
    {
        InitializeCounter(counterName);
        Counters[counterName]--;
    }

    public void Reset(string counterName = "")
    {
        int value = GetValue(counterName);
        if (value == 0 || string.IsNullOrEmpty(counterName))
        {
            foreach (var key in Counters.Keys.ToList())
            {
                Counters[key] = 0;
            }
        }
        else
        {
            Counters[counterName] = 0;
        }
    }

    public Dictionary<string, int> ListCounters()
    {
        return Counters;
    }

}
