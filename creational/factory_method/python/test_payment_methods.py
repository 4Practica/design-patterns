import pytest
from .payment_factory import PaymentFactory, PaymentMethod
from .payment_processors import (
    CreditCardProcessor,
    PayPalProcessor,
    BankTransferProcessor,
    DigitalWalletProcessor,
    PaymentProcessor
)

class TestPaymentFactory:
    def test_create_credit_card_processor(self):
        """Test creating a credit card payment processor"""
        processor = PaymentFactory.create_payment_method(PaymentMethod.CREDIT_CARD)
        assert isinstance(processor, CreditCardProcessor)

    def test_create_paypal_processor(self):
        """Test creating a PayPal payment processor"""
        processor = PaymentFactory.create_payment_method(PaymentMethod.PAYPAL)
        assert isinstance(processor, PayPalProcessor)

    def test_create_bank_transfer_processor(self):
        """Test creating a bank transfer payment processor"""
        processor = PaymentFactory.create_payment_method(PaymentMethod.BANK_TRANSFER)
        assert isinstance(processor, BankTransferProcessor)

    def test_create_digital_wallet_processor(self):
        """Test creating a digital wallet payment processor"""
        processor = PaymentFactory.create_payment_method(PaymentMethod.DIGITAL_WALLET)
        assert isinstance(processor, DigitalWalletProcessor)

    def test_invalid_payment_method(self):
        """Test creating a payment processor with invalid method"""
        with pytest.raises(ValueError):
            PaymentFactory.create_payment_method("INVALID_METHOD") # type: ignore

class TestCreditCardProcessor:
    @pytest.fixture
    def processor(self):
        return CreditCardProcessor()

    def test_validate_data(self, processor: PaymentProcessor):
        """Test credit card data validation"""
        valid_data = {
            "card_number": "4111111111111111",
            "expiry_date": "12/25",
            "cvv": "123"
        }
        assert processor.validate_data(valid_data) is True

        invalid_data = {
            "card_number": "4111111111111111",
            "expiry_date": "12/25",
            "cvv": "12"  # Invalid CVV
        }
        assert processor.validate_data(invalid_data) is False

    def test_calculate_commission(self, processor: PaymentProcessor):
        """Test commission calculation for credit card"""
        amount = 100.00
        commission = processor.calculate_commission(amount)
        assert commission == amount * 0.03  # 3% commission

    def test_process_payment(self, processor: PaymentProcessor):
        """Test payment processing for credit card"""
        payment_data = {
            "card_number": "4111111111111111",
            "expiry_date": "12/25",
            "cvv": "123",
            "amount": 100.00
        }
        result = processor.process_payment(payment_data)
        assert result["success"] is True
        assert "transaction_id" in result

    def test_generate_receipt(self, processor: PaymentProcessor):
        """Test receipt generation for credit card"""
        payment_data = {
            "card_number": "4111111111111111",
            "amount": 100.00,
            "transaction_id": "123456"
        }
        receipt = processor.generate_receipt(payment_data)
        assert "Credit Card Payment" in receipt
        assert "100.00" in receipt
        assert "123456" in receipt

class TestPayPalProcessor:
    @pytest.fixture
    def processor(self):
        return PayPalProcessor()

    def test_validate_data(self, processor: PaymentProcessor):
        """Test PayPal data validation"""
        valid_data = {
            "email": "test@example.com",
            "password": "validpassword"
        }
        assert processor.validate_data(valid_data) is True

    def test_calculate_commission(self, processor: PaymentProcessor):
        """Test commission calculation for PayPal"""
        amount = 100.00
        commission = processor.calculate_commission(amount)
        assert commission == amount * 0.02  # 2% commission

    def test_process_payment(self, processor: PaymentProcessor):
        """Test payment processing for PayPal"""
        payment_data = {
            "email": "test@example.com",
            "amount": 100.00
        }
        result = processor.process_payment(payment_data)
        assert result["success"] is True
        assert "transaction_id" in result

    def test_generate_receipt(self, processor: PaymentProcessor):
        """Test receipt generation for PayPal"""
        payment_data = {
            "email": "test@example.com",
            "amount": 100.00,
            "transaction_id": "123456"
        }
        receipt = processor.generate_receipt(payment_data)
        assert "PayPal Payment" in receipt
        assert "100.00" in receipt
        assert "123456" in receipt

class TestBankTransferProcessor:
    @pytest.fixture
    def processor(self):
        return BankTransferProcessor()

    def test_validate_data(self, processor: PaymentProcessor):
        """Test bank transfer data validation"""
        valid_data = {
            "account_number": "1234567890",
            "routing_number": "987654321",
            "account_holder": "John Doe"
        }
        assert processor.validate_data(valid_data) is True

        invalid_data = {
            "account_number": "123",  # Too short
            "routing_number": "987654321",
            "account_holder": "John Doe"
        }
        assert processor.validate_data(invalid_data) is False

    def test_calculate_commission(self, processor: PaymentProcessor):
        """Test commission calculation for bank transfer"""
        amount = 100.00
        commission = processor.calculate_commission(amount)
        assert commission == amount * 0.01  # 1% commission

    def test_process_payment(self, processor: PaymentProcessor):
        """Test payment processing for bank transfer"""
        payment_data = {
            "account_number": "1234567890",
            "amount": 100.00
        }
        result = processor.process_payment(payment_data)
        assert result["success"] is True
        assert "transaction_id" in result

    def test_generate_receipt(self, processor: PaymentProcessor):
        """Test receipt generation for bank transfer"""
        payment_data = {
            "account_number": "1234567890",
            "amount": 100.00,
            "transaction_id": "123456"
        }
        receipt = processor.generate_receipt(payment_data)
        assert "Bank Transfer" in receipt
        assert "100.00" in receipt
        assert "123456" in receipt

class TestDigitalWalletProcessor:
    @pytest.fixture
    def processor(self):
        return DigitalWalletProcessor()

    def test_validate_data(self, processor: PaymentProcessor):
        """Test digital wallet data validation"""
        valid_data = {
            "wallet_id": "WALLET123",
            "phone_number": "+1234567890"
        }
        assert processor.validate_data(valid_data) is True

        invalid_data = {
            "wallet_id": "WALLET123",
            "phone_number": "invalid-phone"
        }
        assert processor.validate_data(invalid_data) is False

    def test_calculate_commission(self, processor: PaymentProcessor):
        """Test commission calculation for digital wallet"""
        amount = 100.00
        commission = processor.calculate_commission(amount)
        assert commission == amount * 0.015  # 1.5% commission

    def test_process_payment(self, processor: PaymentProcessor):
        """Test payment processing for digital wallet"""
        payment_data = {
            "wallet_id": "WALLET123",
            "amount": 100.00
        }
        result = processor.process_payment(payment_data)
        assert result["success"] is True
        assert "transaction_id" in result

    def test_generate_receipt(self, processor: PaymentProcessor):
        """Test receipt generation for digital wallet"""
        payment_data = {
            "wallet_id": "WALLET123",
            "amount": 100.00,
            "transaction_id": "123456"
        }
        receipt = processor.generate_receipt(payment_data)
        assert "Digital Wallet Payment" in receipt
        assert "100.00" in receipt
        assert "123456" in receipt
