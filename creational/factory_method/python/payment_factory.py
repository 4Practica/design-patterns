from enum import Enum
from typing import Dict, Union
from .payment_processors import (
    CreditCardProcessor,
    PayPalProcessor,
    BankTransferProcessor,
    DigitalWalletProcessor,
    PaymentProcessor
)

class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    DIGITAL_WALLET = "digital_wallet"

class PaymentFactory:
    _platforms: Dict[PaymentMethod, type[PaymentProcessor]] = {
        PaymentMethod.CREDIT_CARD: CreditCardProcessor,
        PaymentMethod.PAYPAL: PayPalProcessor,
        PaymentMethod.BANK_TRANSFER: BankTransferProcessor,
        PaymentMethod.DIGITAL_WALLET: DigitalWalletProcessor
    }

    @classmethod
    def create_payment_method(cls, payment_method: Union[PaymentMethod, str]) -> PaymentProcessor:
        if isinstance(payment_method, str):
            try:
                payment_method = PaymentMethod(payment_method)
            except ValueError:
                raise ValueError(f"Invalid payment method: {payment_method}")

        try:
            return cls._platforms[payment_method]()
        except KeyError:
            raise ValueError(f"Payment processor not implemented for method: {payment_method}")
        