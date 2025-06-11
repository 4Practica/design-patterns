namespace FactoryMethod.Core;

public class PaymentFactory
{
    private static readonly Dictionary<PaymentMethod, Func<object>> _paymentProcessors = new()
    {
        { PaymentMethod.CreditCard, () => new CreditCardProcessor() },
        { PaymentMethod.PayPal, () => new PayPalProcessor() },
        { PaymentMethod.BankTransfer, () => new BankTransferProcessor() },
        { PaymentMethod.DigitalWallet, () => new DigitalWalletProcessor() }
    };

    public static object CreatePaymentMethod(PaymentMethod method)
    {
        if (_paymentProcessors.TryGetValue(method, out Func<object>? processorFactory))
        {
            return processorFactory();
        }

        throw new ArgumentException($"Payment method {method} is not supported.", nameof(method));
    }
}

public enum PaymentMethod
{
    CreditCard,
    PayPal,
    BankTransfer,
    DigitalWallet
}