using System.Diagnostics;
using Xunit;

namespace SampleApp.Tests
{
    public class E2ETests
    {
        [Fact]
        public void ApplicationShouldRunAndOutputExpectedResult()
        {
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "dotnet",
                    Arguments = "run --project ../src/SampleApp.csproj",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };

            process.Start();
            var output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();

            Assert.Contains("Hello, SonarQube!", output);
        }
    }
}
