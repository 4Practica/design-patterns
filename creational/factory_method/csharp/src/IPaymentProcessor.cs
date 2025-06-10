public interface IPaymentProcessor
{
    bool ValidateData(Dictionary<string, string> paymentData);
    double CalculateCommission(double amount);
    Dictionary<string, object> ProcessPayment(object paymentData);
    string GenerateReceipt(object paymentData);
}