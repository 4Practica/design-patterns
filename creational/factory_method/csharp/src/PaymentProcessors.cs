public class CreditCardProcessor : IPaymentProcessor<CreditCardData>
{
    public bool ValidateData(CreditCardData paymentData)
    {
        return !string.IsNullOrEmpty(paymentData.CardNumber) &&
                   paymentData.CardNumber.Length == 16 &&
                   !string.IsNullOrEmpty(paymentData.ExpiryDate) &&
                   paymentData.Cvv != null && paymentData.Cvv.Length == 3;
    }
    public double CalculateCommission(double amount)
    {
        return amount * 0.03;
    }
    public PaymentResult ProcessPayment(CreditCardData paymentData)
    {
        if (ValidateData(paymentData))
        {
            string transactionId = Guid.NewGuid().ToString();
            return new PaymentResult { Success = true, TransactionId = transactionId, Message = "Credit card payment successfully processed." };
        }
        return new PaymentResult { Success = false, TransactionId = "", Message = "Invalid credit card information." };
    }
    public string GenerateReceipt(CreditCardData paymentData)
    {
        return $"Credit Card Payment:\n" +
                $"Amount: {paymentData.Amount:F2}\n" +
                $"Lasts 4 digits of your card: {paymentData.CardNumber?.Substring(paymentData.CardNumber.Length - 4)}\n" +
                $"Transaction ID: {paymentData.TransactionId}";
    }
}

public class PayPalProcessor : IPaymentProcessor<PayPalData>
{
    public bool ValidateData(PayPalData paymentData)
    {
        return !string.IsNullOrEmpty(paymentData.Email) &&
                    paymentData.Email.Contains("@");
    }
    public double CalculateCommission(double amount)
    {
        return amount * 0.02;
    }
    public PaymentResult ProcessPayment(PayPalData paymentData)
    {
        if (ValidateData(paymentData))
        {
            string transactionId = Guid.NewGuid().ToString();
            return new PaymentResult { Success = true, TransactionId = transactionId, Message = "PayPal payment successfully processed." };
        }
        return new PaymentResult { Success = false, TransactionId = "", Message = "Invalid PayPal data." };
    }
    public string GenerateReceipt(PayPalData paymentData)
    {
        return $"PayPal Payment:\n" +
                $"Amount: {paymentData.Amount:F2}\n" +
                $"Email: {paymentData.Email}\n" +
                $"Transaction ID: {paymentData.TransactionId}";
    }
}

public class BankTransferProcessor : IPaymentProcessor<BankTransferData>
{
    public bool ValidateData(BankTransferData paymentData)
    {
        return !string.IsNullOrEmpty(paymentData.AccountNumber) &&
                   paymentData.AccountNumber.Length >= 10;
    }
    public double CalculateCommission(double amount)
    {
        return amount * 0.01;
    }
    public PaymentResult ProcessPayment(BankTransferData paymentData)
    {
        if (ValidateData(paymentData))
        {
            string transactionId = Guid.NewGuid().ToString();
            return new PaymentResult { Success = true, TransactionId = transactionId, Message = "Bank transfer payment successfully processed." };
        }
        return new PaymentResult { Success = false, TransactionId = "", Message = "Invalid bank transfer data." };
    }
    public string GenerateReceipt(BankTransferData paymentData)
    {
        return $"Bank Transfer:\n" +
                $"Amount: {paymentData.Amount:F2}\n" +
                $"Account number: {paymentData.AccountNumber}\n" +
                $"Transaction ID: {paymentData.TransactionId}";
    }
}

public class DigitalWalletProcessor : IPaymentProcessor<DigitalWalletData>
{
    public bool ValidateData(DigitalWalletData paymentData)
    {
        return !string.IsNullOrEmpty(paymentData.WalletId) &&
                   !string.IsNullOrEmpty(paymentData.PhoneNumber) &&
                   paymentData.PhoneNumber.StartsWith("+");
    }
    public double CalculateCommission(double amount)
    {
        return amount * 0.015;
    }
    public PaymentResult ProcessPayment(DigitalWalletData paymentData)
    {
        if (ValidateData(paymentData))
        {
            string transactionId = Guid.NewGuid().ToString();
            return new PaymentResult { Success = true, TransactionId = transactionId, Message = "Digital wallet payment successfully processed." };
        }
        return new PaymentResult { Success = false, TransactionId = "", Message = "Invalid digital wallet data." };
    }
    public string GenerateReceipt(DigitalWalletData paymentData)
    {
        return $"Digital Wallet Payment:\n" +
                $"Amount: {paymentData.Amount:F2}\n" +
                $"Wallet ID: {paymentData.WalletId}\n" +
                $"Transaction ID: {paymentData.TransactionId}";
    }
}