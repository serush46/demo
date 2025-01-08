using Xunit;

namespace SampleApp.Tests
{
    public class ProgramTests
    {
        [Fact]
        public void TestOutput()
        {
            Assert.Equal("Hello, SonarQube!", "Hello, SonarQube!");
        }
    }
}
