const {
    PaymentFactory,
    PaymentMethod,
    CreditCardProcessor,
    PayPalProcessor,
    BankTransferProcessor,
    DigitalWalletProcessor,
} = require('./payment_factory');
const {
    PaymentProcessor,
} = require('./payment_processors');

describe('PaymentFactory', () => {
    test('creates a credit card processor', () => {
        const processor = PaymentFactory.createPaymentMethod(PaymentMethod.CREDIT_CARD);
        expect(processor).toBeInstanceOf(CreditCardProcessor);
    });

    test('creates a PayPal processor', () => {
        const processor = PaymentFactory.createPaymentMethod(PaymentMethod.PAYPAL);
        expect(processor).toBeInstanceOf(PayPalProcessor);
    });

    test('creates a bank transfer processor', () => {
        const processor = PaymentFactory.createPaymentMethod(PaymentMethod.BANK_TRANSFER);
        expect(processor).toBeInstanceOf(BankTransferProcessor);
    });

    test('creates a digital wallet processor', () => {
        const processor = PaymentFactory.createPaymentMethod(PaymentMethod.DIGITAL_WALLET);
        expect(processor).toBeInstanceOf(DigitalWalletProcessor);
    });

    test('throws on invalid payment method', () => {
        expect(() => {
            PaymentFactory.createPaymentMethod('INVALID_METHOD');
        }).toThrow();
    });
});

describe('CreditCardProcessor', () => {
    let processor;
    beforeEach(() => {
        processor = new CreditCardProcessor();
    });

    test('validates credit card data', () => {
        const validData = {
            card_number: '4111111111111111',
            expiry_date: '12/25',
            cvv: '123',
        };
        expect(processor.validateData(validData)).toBe(true);

        const invalidData = {
            card_number: '4111111111111111',
            expiry_date: '12/25',
            cvv: '12', // Invalid CVV
        };
        expect(processor.validateData(invalidData)).toBe(false);
    });

    test('calculates commission', () => {
        const amount = 100.0;
        expect(processor.calculateCommission(amount)).toBe(amount * 0.03);
    });

    test('processes payment', () => {
        const paymentData = {
            card_number: '4111111111111111',
            expiry_date: '12/25',
            cvv: '123',
            amount: 100.0,
        };
        const result = processor.processPayment(paymentData);
        expect(result.success).toBe(true);
        expect(result).toHaveProperty('transaction_id');
    });

    test('generates receipt', () => {
        const paymentData = {
            card_number: '4111111111111111',
            amount: 100.0,
            transaction_id: '123456',
        };
        const receipt = processor.generateReceipt(paymentData);
        expect(receipt).toMatch(/Credit Card Payment/);
        expect(receipt).toMatch(/100\.00/);
        expect(receipt).toMatch(/123456/);
    });
});

describe('PayPalProcessor', () => {
    let processor;
    beforeEach(() => {
        processor = new PayPalProcessor();
    });

    test('validates PayPal data', () => {
        const validData = {
            email: 'test@example.com',
            password: 'validpassword',
        };
        expect(processor.validateData(validData)).toBe(true);
    });

    test('calculates commission', () => {
        const amount = 100.0;
        expect(processor.calculateCommission(amount)).toBe(amount * 0.02);
    });

    test('processes payment', () => {
        const paymentData = {
            email: 'test@example.com',
            amount: 100.0,
        };
        const result = processor.processPayment(paymentData);
        expect(result.success).toBe(true);
        expect(result).toHaveProperty('transaction_id');
    });

    test('generates receipt', () => {
        const paymentData = {
            email: 'test@example.com',
            amount: 100.0,
            transaction_id: '123456',
        };
        const receipt = processor.generateReceipt(paymentData);
        expect(receipt).toMatch(/PayPal Payment/);
        expect(receipt).toMatch(/100\.00/);
        expect(receipt).toMatch(/123456/);
    });
});

describe('BankTransferProcessor', () => {
    let processor;
    beforeEach(() => {
        processor = new BankTransferProcessor();
    });

    test('validates bank transfer data', () => {
        const validData = {
            account_number: '1234567890',
            routing_number: '987654321',
            account_holder: 'John Doe',
        };
        expect(processor.validateData(validData)).toBe(true);

        const invalidData = {
            account_number: '123', // Too short
            routing_number: '987654321',
            account_holder: 'John Doe',
        };
        expect(processor.validateData(invalidData)).toBe(false);
    });

    test('calculates commission', () => {
        const amount = 100.0;
        expect(processor.calculateCommission(amount)).toBe(amount * 0.01);
    });

    test('processes payment', () => {
        const paymentData = {
            account_number: '1234567890',
            amount: 100.0,
        };
        const result = processor.processPayment(paymentData);
        expect(result.success).toBe(true);
        expect(result).toHaveProperty('transaction_id');
    });

    test('generates receipt', () => {
        const paymentData = {
            account_number: '1234567890',
            amount: 100.0,
            transaction_id: '123456',
        };
        const receipt = processor.generateReceipt(paymentData);
        expect(receipt).toMatch(/Bank Transfer/);
        expect(receipt).toMatch(/100\.00/);
        expect(receipt).toMatch(/123456/);
    });
});

describe('DigitalWalletProcessor', () => {
    let processor;
    beforeEach(() => {
        processor = new DigitalWalletProcessor();
    });

    test('validates digital wallet data', () => {
        const validData = {
            wallet_id: 'WALLET123',
            phone_number: '+1234567890',
        };
        expect(processor.validateData(validData)).toBe(true);

        const invalidData = {
            wallet_id: 'WALLET123',
            phone_number: 'invalid-phone',
        };
        expect(processor.validateData(invalidData)).toBe(false);
    });

    test('calculates commission', () => {
        const amount = 100.0;
        expect(processor.calculateCommission(amount)).toBe(amount * 0.015);
    });

    test('processes payment', () => {
        const paymentData = {
            wallet_id: 'WALLET123',
            amount: 100.0,
        };
        const result = processor.processPayment(paymentData);
        expect(result.success).toBe(true);
        expect(result).toHaveProperty('transaction_id');
    });

    test('generates receipt', () => {
        const paymentData = {
            wallet_id: 'WALLET123',
            amount: 100.0,
            transaction_id: '123456',
        };
        const receipt = processor.generateReceipt(paymentData);
        expect(receipt).toMatch(/Digital Wallet Payment/);
        expect(receipt).toMatch(/100\.00/);
        expect(receipt).toMatch(/123456/);
    });
});