public class CreditCardData
{
    public string CardNumber = string.Empty;
    public string ExpiryDate = string.Empty;
    public string Cvv = string.Empty;
    public double Amount;
    public string TransactionId = string.Empty;
}

public class PayPalData
{
    public string Email = string.Empty;
    public string Password = string.Empty;
    public double Amount;
    public string TransactionId = string.Empty;
}

public class BankTransferData
{
    public string AccountNumber = string.Empty;
    public string RoutingNumber = string.Empty;
    public string AccountHolder = string.Empty;
    public double Amount;
    public string TransactionId = string.Empty;
}

public class DigitalWalletData
{
    public string WalletId = string.Empty;
    public string PhoneNumber = string.Empty;
    public double Amount;
    public string TransactionId = string.Empty;
}