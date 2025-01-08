using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace SampleApp.Tests
{
    [TestClass]
    public class UnitTests
    {
        [TestMethod]
        public void TestHelloWorld()
        {
            string expected = "Hello, World!";
            string actual = GetHelloWorldMessage();
            Assert.AreEqual(expected, actual);
        }

        private string GetHelloWorldMessage()
        {
            return "Hello, World!";
        }
    }
}
