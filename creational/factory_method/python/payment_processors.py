from abc import ABC, abstractmethod
import re

class PaymentProcessor(ABC):
    @abstractmethod
    def validate_data(self, data: dict[str, str]) -> bool:
        pass

    @abstractmethod
    def calculate_commission(self, amount: float) -> float:
        pass
    
    @abstractmethod
    def process_payment(self, data: dict[str, str | float]) -> dict[str, str | bool | float]:
        pass

    @abstractmethod
    def generate_receipt(self, data: dict[str, str | float]) -> str:
        pass



class CreditCardProcessor(PaymentProcessor):
    def validate_data(self, data: dict[str, str]) -> bool:
        required_fields = ["card_number", "expiry_date", "cvv"]
        is_valid = all(field in data for field in required_fields)
        cvv_is_valid = len(data.get("cvv")) >= 3 # type: ignore
        return is_valid and cvv_is_valid

    def calculate_commission(self, amount: float) -> float:
        return amount * 0.03  # 3% commission
    
    def process_payment(self, data: dict[str, str | float]) -> dict[str, str | bool | float]:
        return {
            "success": True,
            "transaction_id": "CC-" + str(hash(str(data))),
            "amount": data.get("amount", 0.0)
        }

    def generate_receipt(self, data: dict[str, str | float]) -> str:
        return f"Credit Card Payment Receipt\nAmount: {"%.2f" % round(float(data.get('amount', 0.00)), 2)} \nTransaction ID: {data.get('transaction_id', 'N/A')}"

class PayPalProcessor(PaymentProcessor):
    def validate_data(self, data: dict[str, str]) -> bool:
        required_fields = ["email", "password"]
        return all(field in data for field in required_fields)

    def calculate_commission(self, amount: float) -> float:
        return amount * 0.02  # 2% commission
    
    def process_payment(self, data: dict[str, str | float]) -> dict[str, str | bool | float]:
        return {
            "success": True,
            "transaction_id": "PP-" + str(hash(str(data))),
            "amount": data.get("amount", 0.0)
        }

    def generate_receipt(self, data: dict[str, str | float]) -> str:
        return f"PayPal Payment Receipt\nAmount: {"%.2f" % round(float(data.get('amount', 0.00)), 2)}\nTransaction ID: {data.get('transaction_id', 'N/A')}"

class BankTransferProcessor(PaymentProcessor):
    def validate_data(self, data: dict[str, str]) -> bool:
        required_fields = ["account_number", "routing_number", "account_holder"]
        present_data = all(field in data for field in required_fields)
        account_number_is_valid = len(data.get("account_number", "")) > 9
        return present_data and account_number_is_valid
    def calculate_commission(self, amount: float) -> float:
        return amount * 0.01  # 1% commission
    
    def process_payment(self, data: dict[str, str | float]) -> dict[str, str | bool | float]:
        return {
            "success": True,
            "transaction_id": "BT-" + str(hash(str(data))),
            "amount": data.get("amount", 0.0)
        }

    def generate_receipt(self, data: dict[str, str | float]) -> str:
        return f"Bank Transfer Receipt\nAmount: {"%.2f" % round(float(data.get('amount', 0.00)), 2)}\nTransaction ID: {data.get('transaction_id', 'N/A')}"

class DigitalWalletProcessor(PaymentProcessor):
    def _validate_phone_number(self, phone: str) -> bool:
        """
        Validate phone number format.
        Supports formats:
        - International: +1-234-567-8900, +1.234.567.8900, +1 234 567 8900
        - National: (234) 567-8900, 234-567-8900, 234.567.8900
        - Simple: 2345678900
        """
        # Remove any spaces, dashes, dots, or parentheses
        phone = re.sub(r'[\s\-\.\(\)]', '', phone)
        
        # Check if it's an international number (starts with +)
        if phone.startswith('+'):
            # International format: +1-234-567-8900 (10-15 digits after +)
            pattern = r'^\+\d{10,15}$'
        else:
            # National format: (234) 567-8900 (10 digits)
            pattern = r'^\d{10}$'
        
        return bool(re.match(pattern, phone))

    def validate_data(self, data: dict[str, str]) -> bool:
        required_fields = ["wallet_id", "phone_number"]
        if not all(field in data for field in required_fields):
            return False
        
        # Validate phone number format
        return self._validate_phone_number(data["phone_number"])

    def calculate_commission(self, amount: float) -> float:
        return amount * 0.015  # 1.5% commission
    
    def process_payment(self, data: dict[str, str | float]) -> dict[str, str | bool | float]:
        return {
            "success": True,
            "transaction_id": "DW-" + str(hash(str(data))),
            "amount": data.get("amount", 0.0)
        }

    def generate_receipt(self, data: dict[str, str | float]) -> str:
        return f"Digital Wallet Payment Receipt\nAmount: {"%.2f" % round(float(data.get('amount', 0.00)), 2)}\nTransaction ID: {data.get('transaction_id', 'N/A')}"