namespace Singleton.Core;

public class GlobalCounter
{
    private static GlobalCounter? _instance;
    private Dictionary<string, int> _counters;

    private GlobalCounter()
    {
        _counters = new Dictionary<string, int>();
    }

    public static GlobalCounter GetInstance()
    {
        _instance ??= new GlobalCounter();
        return _instance;
    }

    public static void ResetInstance()
    {
        _instance = null; // Esto es lo que asegura una nueva instancia
    }

    public int GetValue(string counterName)
    {
        _counters.TryGetValue(counterName, out int value);
        return value;
    }

    public void Increment(string counterName)
    {
        int value = GetValue(counterName);
        if (value == 0)
            _counters[counterName] = 1;
        else
            _counters[counterName]++;
    }

    public void Decrement(string counterName)
    {
        int value = GetValue(counterName);
        if (value == 0)
            _counters[counterName] = -1;
        else
            _counters[counterName]--;

    }

    public void Reset(string counterName = "")
    {
        if (string.IsNullOrEmpty(counterName))
        {
            _counters.Clear();
        }
        else
        {
            _counters[counterName] = 0;
        }
    }

    public Dictionary<string, int> ListCounters()
    {
        return new Dictionary<string, int>(_counters);
    }

}
