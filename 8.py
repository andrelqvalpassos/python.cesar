def celsius_para_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
