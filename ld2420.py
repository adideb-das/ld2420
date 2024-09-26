import serial
import time
import pandas as pd
import re

ser = serial.Serial(port='/dev/ttyS0', baudrate=115200, timeout=1)

def extract_numbers(input_data):
    
    if isinstance(input_data, bytes):
        input_string = input_data.decode('utf-8', errors='ignore')
    else:
        input_string = input_data    

    numbers = re.findall(r'\d+', input_string)    
    
    return ''.join(numbers) if numbers else None

def detect_distance(value):
    if value is None:
        return "No valid numeric value detected!"
    
    try:
        value = int(value)
    except ValueError:
        return "----------------------------------"
    
    if 0 <= value < 100:
        return "Detected at 1 meter"
    elif 100 <= value < 200:
        return "Detected at 2 meters"
    elif 200 <= value < 300:
        return "Detected at 3 meters"
    elif 300 <= value < 400:
        return "Detected at 4 meters"
    elif 400 <= value < 500:
        return "Detected at 5 meters"
    elif 500 <= value < 600:
        return "Detected at 6 meters"
    elif 600 <= value < 700:
        return "Detected at 7 meters"
    elif 700 <= value < 800:
        return "Detected at 8 meters"
    else:
        return "Value out of range"

while True:
    try:
        value = ser.readline()
        value2 = extract_numbers(value)
        
        if value2 is not None:
            print(f"Raw value: {value2}")
            message = detect_distance(value2)
            print(message)
        else:
            print("------------.")

        time.sleep(0.7)  # Optional: Add a sleep to avoid flooding the output

    except serial.SerialException as e:
        print(f"Serial error: {e}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break
