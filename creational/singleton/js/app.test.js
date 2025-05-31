const GlobalCounter = require('./globalCounter');

describe('GlobalCounter', () => {
    // Limpiar la instancia antes de cada test
    beforeEach(() => {
        GlobalCounter.resetInstance();
    });
    
    describe('Singleton Pattern', () => {
        test('should return same instance when created multiple times', () => {
            const counter1 = new GlobalCounter();
            const counter2 = new GlobalCounter();
            
            expect(counter1 === counter2).toBe(true);
        });
        
        test('should share state between instances', () => {
            const counter1 = new GlobalCounter();
            const counter2 = new GlobalCounter();
            
            counter1.increment('visits');
            expect(counter2.getValue('visits')).toBe(1);
        });
    });
    
    describe('increment method', () => {
        test('should increment counter by 1', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            expect(counter.getValue('visits')).toBe(1);
            
            counter.increment('visits');
            expect(counter.getValue('visits')).toBe(2);
        });
        
        test('should create new counter if it does not exist', () => {
            const counter = new GlobalCounter();
            
            counter.increment('newCounter');
            expect(counter.getValue('newCounter')).toBe(1);
        });
        
        test('should handle multiple different counters', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('errors');
            counter.increment('visits');
            
            expect(counter.getValue('visits')).toBe(2);
            expect(counter.getValue('errors')).toBe(1);
        });
    });
    
    describe('decrement method', () => {
        test('should decrement counter by 1', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('visits');
            counter.decrement('visits');
            
            expect(counter.getValue('visits')).toBe(1);
        });
        
        test('should create counter with 0 and decrement to -1', () => {
            const counter = new GlobalCounter();
            
            counter.decrement('newCounter');
            expect(counter.getValue('newCounter')).toBe(-1);
        });
    });
    
    describe('reset method', () => {
        test('should reset specific counter to 0', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('visits');
            counter.reset('visits');
            
            expect(counter.getValue('visits')).toBe(0);
        });
        
        test('should reset all counters when no name provided', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('errors');
            counter.reset();
            
            expect(counter.getValue('visits')).toBe(0);
            expect(counter.getValue('errors')).toBe(0);
        });
    });
    
    describe('getValue method', () => {
        test('should return current value of counter', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('visits');
            
            expect(counter.getValue('visits')).toBe(2);
        });
        
        test('should return 0 for non-existing counter', () => {
            const counter = new GlobalCounter();
            
            expect(counter.getValue('nonExistent')).toBe(0);
        });
    });
    
    describe('listCounters method', () => {
        test('should return empty object when no counters exist', () => {
            const counter = new GlobalCounter();
            
            expect(counter.listCounters()).toEqual({});
        });
        
        test('should return all counters with their values', () => {
            const counter = new GlobalCounter();
            
            counter.increment('visits');
            counter.increment('visits');
            counter.increment('errors');
            
            const counters = counter.listCounters();
            expect(counters).toEqual({
                visits: 2,
                errors: 1
            });
        });
    });
    
    describe('Integration tests', () => {
        test('should work correctly with mixed operations', () => {
            const counter = new GlobalCounter();
            
            // Crear varios contadores
            counter.increment('visits');
            counter.increment('visits');
            counter.increment('errors');
            counter.decrement('warnings');
            
            // Verificar valores
            expect(counter.getValue('visits')).toBe(2);
            expect(counter.getValue('errors')).toBe(1);
            expect(counter.getValue('warnings')).toBe(-1);
            
            // Resetear uno específico
            counter.reset('visits');
            expect(counter.getValue('visits')).toBe(0);
            expect(counter.getValue('errors')).toBe(1);
        });
        
        test('should maintain state across different instances', () => {
            const counter1 = new GlobalCounter();
            const counter2 = new GlobalCounter();
            
            counter1.increment('visits');
            counter2.increment('visits');
            counter1.increment('errors');
            
            expect(counter2.getValue('visits')).toBe(2);
            expect(counter1.getValue('errors')).toBe(1);
            
            const allCounters = counter2.listCounters();
            expect(allCounters.visits).toBe(2);
            expect(allCounters.errors).toBe(1);
        });
    });
});
