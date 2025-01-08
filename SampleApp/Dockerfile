# Use the .NET 6 SDK image
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
WORKDIR /app

# Copy and restore project files
COPY ./src/SampleApp.csproj ./src/
RUN dotnet restore ./src/SampleApp.csproj

# Copy the source code and build the application
COPY ./src ./src
RUN dotnet publish ./src/SampleApp.csproj -c Release -o out

# Build a runtime image
FROM mcr.microsoft.com/dotnet/runtime:6.0
WORKDIR /app
COPY --from=build-env /app/out .

# Set the entry point for the application
ENTRYPOINT ["dotnet", "SampleApp.dll"]
