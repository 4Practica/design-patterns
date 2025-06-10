public class CreditCardProcessor : IPaymentProcessor
{
    public bool ValidateData(Dictionary<string, string> paymentData)
    {
        return true;
    }
    public double CalculateCommission(double amount)
    {
        return 0.1d;
    }
    public Dictionary<string, object> ProcessPayment(object paymentData)
    {
        return new Dictionary<string, object>();
    }
    public string GenerateReceipt(object paymentData)
    {
        return "hola";
    }
}

public class PayPalProcessor : IPaymentProcessor
{
    public bool ValidateData(Dictionary<string, string> paymentData)
    {
        return true;
    }
    public double CalculateCommission(double amount)
    {
        return 0.1d;
    }
    public Dictionary<string, object> ProcessPayment(object paymentData)
    {
        return new Dictionary<string, object>();
    }
    public string GenerateReceipt(object paymentData)
    {
        return "hola";
    }
}

public class BankTransferProcessor : IPaymentProcessor
{
    public bool ValidateData(Dictionary<string, string> paymentData)
    {
        return true;
    }
    public double CalculateCommission(double amount)
    {
        return 0.1d;
    }
    public Dictionary<string, object> ProcessPayment(object paymentData)
    {
        return new Dictionary<string, object>();
    }
    public string GenerateReceipt(object paymentData)
    {
        return "hola";
    }
}

public class DigitalWalletProcessor : IPaymentProcessor
{
    public bool ValidateData(Dictionary<string, string> paymentData)
    {
        return true;
    }
    public double CalculateCommission(double amount)
    {
        return 0.1d;
    }
    public Dictionary<string, object> ProcessPayment(object paymentData)
    {
        return new Dictionary<string, object>();
    }
    public string GenerateReceipt(object paymentData)
    {
        return "hola";
    }
}