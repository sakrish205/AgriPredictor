import serial
import time
import pickle
import pandas as pd
import schedule
import re  # For regex parsing

# Load the trained model and fertilizer encoding
with open('best_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('fertilizer_encoding.pkl', 'rb') as encoding_file:
    fertilizer_encoding = pickle.load(encoding_file)

# Setup Serial Communication
ser = serial.Serial('COM4', 115200, timeout=1)
time.sleep(3)

def read_sensor_data():
    print("Getting data...")

    moisture_values = []
    humidity_values = []
    temperature_values = []

    start_time = time.time()
    while time.time() - start_time < 5:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()
                print(f"Raw Data: {data}")

                # Parse using regex to extract numbers
                match = re.search(r"Humidity:\s*([\d.]+)%\s*\|\s*Temperature:\s*([\d.]+)°C\s*\|\s*Soil Moisture:\s*([\d]+)%", data)
                if match:
                    humidity, temperature, soil_moisture = map(float, match.groups())
                    humidity_values.append(humidity)
                    temperature_values.append(temperature)
                    moisture_values.append(soil_moisture)
            except Exception as e:
                print("Error:", e)

    if moisture_values:
        avg_moisture = sum(moisture_values) / len(moisture_values)
        avg_temperature = sum(temperature_values) / len(temperature_values)
        avg_humidity = sum(humidity_values) / len(humidity_values)

        # Predict Fertilizer
        input_data = pd.DataFrame([[avg_moisture, avg_humidity, avg_temperature]],
                                  columns=['Moisture', 'Humidity', 'Temparature'])
        prediction = model.predict(input_data)[0]
        predicted_fertilizer = next(
            (fertilizer for fertilizer, value in fertilizer_encoding.items() if value == prediction),
            "Unknown"
        )

        print(f"Average Moisture: {avg_moisture:.2f}%")
        print(f"Average Humidity: {avg_humidity:.2f}%")
        print(f"Average Temperature: {avg_temperature:.2f}°C")
        print(f"Predicted Fertilizer: {predicted_fertilizer}")

    else:
        print("No valid data received.")
# Schedule the function to run every 10 seconds
schedule.every(10).seconds.do(read_sensor_data)

# Run schedule indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
