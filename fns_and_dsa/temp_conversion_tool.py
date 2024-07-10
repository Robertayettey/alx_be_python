# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    while True:
        try:
            temperature_str = input("Enter the temperature (e.g., 32F or 0C): ").strip().upper()
            if temperature_str[-1] == 'F':
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}F is {converted_temp:.2f}C")
                break
            elif temperature_str[-1] == 'C':
                temperature = float(temperature_str[:-1])
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}C is {converted_temp:.2f}F")
                break
            else:
                raise ValueError("Invalid temperature format. Please enter in the format like '32F' or '0C'.")
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()

