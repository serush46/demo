using Xunit;

namespace SampleApp.Tests
{
    public class IntegrationTests
    {
        [Fact]
        public void ServiceShouldReturnExpectedResult()
        {
            var service = new MyService();
            var result = service.ProcessData("input");
            Assert.Equal("processed input", result);
        }
    }

    public class MyService
    {
        public string ProcessData(string data)
        {
            return $"processed {data}";
        }
    }
}
