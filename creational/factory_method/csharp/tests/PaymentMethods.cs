using Xunit;
using FactoryMethod.Core; // Ajusta el namespace según tu estructura real

namespace FactoryMethod.Tests
{
    public class PaymentFactoryTests
    {
        [Fact]
        public void CreatesCreditCardProcessor()
        {
            var processor = PaymentFactory.CreatePaymentMethod(PaymentMethod.CreditCard);
            Assert.IsType<CreditCardProcessor>(processor);
        }

        [Fact]
        public void CreatesPayPalProcessor()
        {
            var processor = PaymentFactory.CreatePaymentMethod(PaymentMethod.PayPal);
            Assert.IsType<PayPalProcessor>(processor);
        }

        [Fact]
        public void CreatesBankTransferProcessor()
        {
            var processor = PaymentFactory.CreatePaymentMethod(PaymentMethod.BankTransfer);
            Assert.IsType<BankTransferProcessor>(processor);
        }

        [Fact]
        public void CreatesDigitalWalletProcessor()
        {
            var processor = PaymentFactory.CreatePaymentMethod(PaymentMethod.DigitalWallet);
            Assert.IsType<DigitalWalletProcessor>(processor);
        }

        [Fact]
        public void ThrowsOnInvalidPaymentMethod()
        {
            Assert.Throws<ArgumentException>(() =>
            {
                PaymentFactory.CreatePaymentMethod((PaymentMethod)999);
            });
        }
    }

    public class CreditCardProcessorTests
    {
        private readonly CreditCardProcessor processor = new CreditCardProcessor();

        [Fact]
        public void ValidatesCreditCardData()
        {
            var validData = new CreditCardData
            {
                CardNumber = "4111111111111111",
                ExpiryDate = "12/25",
                Cvv = "123"
            };
            Assert.True(processor.ValidateData(validData));

            var invalidData = new CreditCardData
            {
                CardNumber = "4111111111111111",
                ExpiryDate = "12/25",
                Cvv = "12"
            };
            Assert.False(processor.ValidateData(invalidData));
        }

        [Fact]
        public void CalculatesCommission()
        {
            double amount = 100.0;
            Assert.Equal(amount * 0.03, processor.CalculateCommission(amount));
        }

        [Fact]
        public void ProcessesPayment()
        {
            var paymentData = new CreditCardData
            {
                CardNumber = "4111111111111111",
                ExpiryDate = "12/25",
                Cvv = "123",
                Amount = 100.0
            };
            var result = processor.ProcessPayment(paymentData);
            Assert.True(result.Success);
            Assert.False(string.IsNullOrEmpty(result.TransactionId));
        }

        [Fact]
        public void GeneratesReceipt()
        {
            var paymentData = new CreditCardData
            {
                CardNumber = "4111111111111111",
                Amount = 100.0,
                TransactionId = "123456"
            };
            var receipt = processor.GenerateReceipt(paymentData);
            Assert.Contains("Credit Card Payment", receipt);
            Assert.Contains("100.00", receipt);
            Assert.Contains("123456", receipt);
        }
    }

    public class PayPalProcessorTests
    {
        private readonly PayPalProcessor processor = new PayPalProcessor();

        [Fact]
        public void ValidatesPayPalData()
        {
            var validData = new PayPalData
            {
                Email = "test@example.com",
                Password = "validpassword"
            };
            Assert.True(processor.ValidateData(validData));
        }

        [Fact]
        public void CalculatesCommission()
        {
            double amount = 100.0;
            Assert.Equal(amount * 0.02, processor.CalculateCommission(amount));
        }

        [Fact]
        public void ProcessesPayment()
        {
            var paymentData = new PayPalData
            {
                Email = "test@example.com",
                Amount = 100.0
            };
            var result = processor.ProcessPayment(paymentData);
            Assert.True(result.Success);
            Assert.False(string.IsNullOrEmpty(result.TransactionId));
        }

        [Fact]
        public void GeneratesReceipt()
        {
            var paymentData = new PayPalData
            {
                Email = "test@example.com",
                Amount = 100.0,
                TransactionId = "123456"
            };
            var receipt = processor.GenerateReceipt(paymentData);
            Assert.Contains("PayPal Payment", receipt);
            Assert.Contains("100.00", receipt);
            Assert.Contains("123456", receipt);
        }
    }

    public class BankTransferProcessorTests
    {
        private readonly BankTransferProcessor processor = new BankTransferProcessor();

        [Fact]
        public void ValidatesBankTransferData()
        {
            var validData = new BankTransferData
            {
                AccountNumber = "1234567890",
                RoutingNumber = "987654321",
                AccountHolder = "John Doe"
            };
            Assert.True(processor.ValidateData(validData));

            var invalidData = new BankTransferData
            {
                AccountNumber = "123",
                RoutingNumber = "987654321",
                AccountHolder = "John Doe"
            };
            Assert.False(processor.ValidateData(invalidData));
        }

        [Fact]
        public void CalculatesCommission()
        {
            double amount = 100.0;
            Assert.Equal(amount * 0.01, processor.CalculateCommission(amount));
        }

        [Fact]
        public void ProcessesPayment()
        {
            var paymentData = new BankTransferData
            {
                AccountNumber = "1234567890",
                Amount = 100.0
            };
            var result = processor.ProcessPayment(paymentData);
            Assert.True(result.Success);
            Assert.False(string.IsNullOrEmpty(result.TransactionId));
        }

        [Fact]
        public void GeneratesReceipt()
        {
            var paymentData = new BankTransferData
            {
                AccountNumber = "1234567890",
                Amount = 100.0,
                TransactionId = "123456"
            };
            var receipt = processor.GenerateReceipt(paymentData);
            Assert.Contains("Bank Transfer", receipt);
            Assert.Contains("100.00", receipt);
            Assert.Contains("123456", receipt);
        }
    }

    public class DigitalWalletProcessorTests
    {
        private readonly DigitalWalletProcessor processor = new DigitalWalletProcessor();

        [Fact]
        public void ValidatesDigitalWalletData()
        {
            var validData = new DigitalWalletData
            {
                WalletId = "WALLET123",
                PhoneNumber = "+1234567890"
            };
            Assert.True(processor.ValidateData(validData));

            var invalidData = new DigitalWalletData
            {
                WalletId = "WALLET123",
                PhoneNumber = "invalid-phone"
            };
            Assert.False(processor.ValidateData(invalidData));
        }

        [Fact]
        public void CalculatesCommission()
        {
            double amount = 100.0;
            Assert.Equal(amount * 0.015, processor.CalculateCommission(amount));
        }

        [Fact]
        public void ProcessesPayment()
        {
            var paymentData = new DigitalWalletData
            {
                WalletId = "WALLET123",
                Amount = 100.0,
                PhoneNumber = "+1234567890"
            };
            var result = processor.ProcessPayment(paymentData);
            Assert.True(result.Success);
            Assert.False(string.IsNullOrEmpty(result.TransactionId));
        }

        [Fact]
        public void GeneratesReceipt()
        {
            var paymentData = new DigitalWalletData
            {
                WalletId = "WALLET123",
                Amount = 100.0,
                TransactionId = "123456"
            };
            var receipt = processor.GenerateReceipt(paymentData);
            Assert.Contains("Digital Wallet Payment", receipt);
            Assert.Contains("100.00", receipt);
            Assert.Contains("123456", receipt);
        }
    }
}