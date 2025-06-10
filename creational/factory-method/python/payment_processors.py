from payment_factory import PaymentMethodInterface

class CreditCardProcessor(PaymentMethodInterface):
    pass

class PayPalProcessor(PaymentMethodInterface):
    pass

class BankTransferProcessor(PaymentMethodInterface):
    pass

class DigitalWalletProcessor(PaymentMethodInterface):
    pass