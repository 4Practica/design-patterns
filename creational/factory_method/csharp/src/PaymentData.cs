public abstract class PaymentData
{
    public double Amount;
    public string TransactionId = string.Empty;
}

public class CreditCardData : PaymentData
{
    public string CardNumber = string.Empty;
    public string ExpiryDate = string.Empty;
    public string Cvv = string.Empty;
}

public class PayPalData : PaymentData
{
    public string Email = string.Empty;
    public string Password = string.Empty;
}

public class BankTransferData : PaymentData
{
    public string AccountNumber = string.Empty;
    public string RoutingNumber = string.Empty;
    public string AccountHolder = string.Empty;
}

public class DigitalWalletData : PaymentData
{
    public string WalletId = string.Empty;
    public string PhoneNumber = string.Empty;
}

public class PaymentResult
{
    public bool Success;
    public string TransactionId = string.Empty;
    public string Message = string.Empty;
}