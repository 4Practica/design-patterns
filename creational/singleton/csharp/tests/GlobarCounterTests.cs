using Singleton.Core; // Para ToDictionary

public class GlobalCounterTests
{
    // Limpiar la instancia antes de cada test.
    // Xunit no tiene un beforeEach directo para cada test como Jest.
    // La forma idiomática es usar el constructor de la clase de prueba y la interfaz IDisposable,
    // o asegurar que cada test obtiene una instancia limpia de la forma en que lo haces en JS.
    // Para replicar el comportamiento de tu JS, llamamos a ResetInstance en cada test donde sea necesario,
    // o al inicio de cada clase de test si usas 'CollectionFixture' para escenarios más complejos.
    // Aquí, replicamos el beforeEach del JS llamando a ResetInstance en el constructor o al inicio de cada test.

    public GlobalCounterTests()
    {
        // Esto se ejecuta antes de cada test en esta clase
        GlobalCounter.ResetInstance();
    }

    public class SingletonPattern
    {
        // Se ejecuta antes de cada test dentro de esta clase anidada
        public SingletonPattern()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldReturnSameInstanceWhenCreatedMultipleTimes()
        {
            GlobalCounter.ResetInstance();
            var counter1 = GlobalCounter.GetInstance();
            var counter2 = GlobalCounter.GetInstance();

            Assert.Same(counter1, counter2); // Assert.Same verifica que las referencias de los objetos sean las mismas
        }

        [Fact]
        public void ShouldShareStateBetweenInstances()
        {
            GlobalCounter.ResetInstance();
            var counter1 = GlobalCounter.GetInstance();
            var counter2 = GlobalCounter.GetInstance();

            counter1.Increment("visits");
            Assert.Equal(1, counter2.GetValue("visits"));
        }
    }

    public class IncrementMethod
    {
        public IncrementMethod()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldIncrementCounterBy1()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            Assert.Equal(1, counter.GetValue("visits"));

            counter.Increment("visits");
            Assert.Equal(2, counter.GetValue("visits"));
        }

        [Fact]
        public void ShouldCreateNewCounterIfItDoesNotExist()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("newCounter");
            Assert.Equal(1, counter.GetValue("newCounter"));
        }

        [Fact]
        public void ShouldHandleMultipleDifferentCounters()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("errors");
            counter.Increment("visits");

            Assert.Equal(2, counter.GetValue("visits"));
            Assert.Equal(1, counter.GetValue("errors"));
        }
    }

    public class DecrementMethod
    {
        public DecrementMethod()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldDecrementCounterBy1()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("visits");
            counter.Decrement("visits");

            Assert.Equal(1, counter.GetValue("visits"));
        }

        [Fact]
        public void ShouldCreateCounterWith0AndDecrementToMinus1()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Decrement("newCounter");
            Assert.Equal(-1, counter.GetValue("newCounter"));
        }
    }

    public class ResetMethod
    {
        public ResetMethod()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldResetSpecificCounterTo0()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("visits");
            counter.Reset("visits");

            Assert.Equal(0, counter.GetValue("visits"));
        }

        [Fact]
        public void ShouldResetAllCountersWhenNoNameProvided()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("errors");
            counter.Reset();

            Assert.Equal(0, counter.GetValue("visits"));
            Assert.Equal(0, counter.GetValue("errors"));
        }
    }

    public class GetValueMethod
    {
        public GetValueMethod()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldReturnCurrentValueOfCounter()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("visits");

            Assert.Equal(2, counter.GetValue("visits"));
        }

        [Fact]
        public void ShouldReturn0ForNonExistingCounter()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            Assert.Equal(0, counter.GetValue("nonExistent"));
        }
    }

    public class ListCountersMethod
    {
        public ListCountersMethod()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldReturnEmptyObjectWhenNoCountersExist()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            Assert.Empty(counter.ListCounters());
            // También se podría Assert.Equal(new Dictionary<string, int>(), counter.ListCounters());
        }

        [Fact]
        public void ShouldReturnAllCountersWithTheirValues()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            counter.Increment("visits");
            counter.Increment("visits");
            counter.Increment("errors");

            var expectedCounters = new Dictionary<string, int>
            {
                { "visits", 2 },
                { "errors", 1 }
            };

            // Para comparar diccionarios, es mejor verificar cada elemento o usar LINQ
            // o un método de extensión si necesitas comparar la igualdad estructural completa.
            // Para diccionarios pequeños, esta comparación simple es suficiente.
            var actualCounters = counter.ListCounters();
            Assert.Equal(expectedCounters.Count, actualCounters.Count);
            foreach (var item in expectedCounters)
            {
                Assert.True(actualCounters.ContainsKey(item.Key));
                Assert.Equal(item.Value, actualCounters[item.Key]);
            }
        }
    }

    public class IntegrationTests
    {
        public IntegrationTests()
        {
            GlobalCounter.ResetInstance();
        }

        [Fact]
        public void ShouldWorkCorrectlyWithMixedOperations()
        {
            GlobalCounter.ResetInstance();
            var counter = GlobalCounter.GetInstance();

            // Crear varios contadores
            counter.Increment("visits");
            counter.Increment("visits");
            counter.Increment("errors");
            counter.Decrement("warnings");

            // Verificar valores
            Assert.Equal(2, counter.GetValue("visits"));
            Assert.Equal(1, counter.GetValue("errors"));
            Assert.Equal(-1, counter.GetValue("warnings"));

            // Resetear uno específico
            counter.Reset("visits");
            Assert.Equal(0, counter.GetValue("visits"));
            Assert.Equal(1, counter.GetValue("errors"));
            // Aquí no se verifica 'warnings' porque el test de JS tampoco lo hace explícitamente en esta parte.
        }

        [Fact]
        public void ShouldMaintainStateAcrossDifferentInstances()
        {
            GlobalCounter.ResetInstance();
            var counter1 = GlobalCounter.GetInstance();
            var counter2 = GlobalCounter.GetInstance();

            counter1.Increment("visits");
            counter2.Increment("visits");
            counter1.Increment("errors");

            Assert.Equal(2, counter2.GetValue("visits"));
            Assert.Equal(1, counter1.GetValue("errors"));

            var allCounters = counter2.ListCounters();
            Assert.Equal(2, allCounters["visits"]);
            Assert.Equal(1, allCounters["errors"]);
        }
    }
}