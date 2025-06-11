public interface IPaymentProcessor<T> where T : PaymentData
{
    bool ValidateData(T paymentData);
    double CalculateCommission(double amount);
    PaymentResult ProcessPayment(T paymentData);
    string GenerateReceipt(T paymentData);
}