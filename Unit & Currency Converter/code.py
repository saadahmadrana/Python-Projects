def length_converter(value, from_unit, to_unit):
    conversion_to_meters = {
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000,
        'inch': 0.0254, 'foot': 0.3048, 'yard': 0.9144, 'mile': 1609.34
    }
    if from_unit not in conversion_to_meters or to_unit not in conversion_to_meters:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    
    meters = value * conversion_to_meters[from_unit]
    return meters / conversion_to_meters[to_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_to_kg = {
        'kg': 1, 'g': 0.001, 'mg': 0.000001, 'lb': 0.453592, 
        'oz': 0.0283495, 'tonne': 1000
    }
    if from_unit not in conversion_to_kg or to_unit not in conversion_to_kg:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    
    kg = value * conversion_to_kg[from_unit]
    return kg / conversion_to_kg[to_unit]

def temperature_converter(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    
    if from_unit == to_unit:
        return value
    
    if from_unit == 'C':
        if to_unit == 'F':
            return value * 9/5 + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError(f"Unsupported temperature units: {from_unit}, {to_unit}")

def currency_converter(value, from_currency, to_currency, exchange_rate):
    return value * exchange_rate

def unit_converter():
    while True:
        print("\nSelect the type of conversion you want to perform:")
        print("1. Length\n2. Weight\n3. Temperature\n4. Currency\n5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        try:
            if choice == '1':
                value = float(input("Enter the value to convert: "))
                from_unit = input("Enter the unit to convert from (e.g., m, cm, km, etc.): ").lower()
                to_unit = input("Enter the unit to convert to: ").lower()
                result = length_converter(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
            
            elif choice == '2':
                value = float(input("Enter the value to convert: "))
                from_unit = input("Enter the unit to convert from (e.g., kg, g, lb, etc.): ").lower()
                to_unit = input("Enter the unit to convert to: ").lower()
                result = weight_converter(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
            
            elif choice == '3':
                value = float(input("Enter the temperature to convert: "))
                from_unit = input("Enter the unit to convert from (C, F, K): ").upper()
                to_unit = input("Enter the unit to convert to: ").upper()
                result = temperature_converter(value, from_unit, to_unit)
                print(f"{value}°{from_unit} = {result}°{to_unit}")
            
            elif choice == '4':
                value = float(input("Enter the amount to convert: "))
                from_currency = input("Enter the currency to convert from (e.g., USD, EUR, PKR): ").upper()
                to_currency = input("Enter the currency to convert to: ").upper()
                exchange_rate = float(input(f"Enter the exchange rate from {from_currency} to {to_currency}: "))
                result = currency_converter(value, from_currency, to_currency, exchange_rate)
                print(f"{value} {from_currency} = {result} {to_currency}")
            
            elif choice == '5':
                print("Exiting the converter. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    unit_converter()
