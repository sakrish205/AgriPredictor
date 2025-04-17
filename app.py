import serial
import time
import pickle
import pandas as pd
import schedule
import re
from flask import Flask, jsonify, render_template
import threading
import os

# Load the trained model and encoding
with open('best_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('fertilizer_encoding.pkl', 'rb') as encoding_file:
    fertilizer_encoding = pickle.load(encoding_file)

# Flask app setup
app = Flask(__name__)

# Try opening the serial port
try:
    ser = serial.Serial('COM4', 115200, timeout=1)
    time.sleep(3)
    print("Serial port opened successfully!")
except Exception as e:
    print("Error opening serial port:", e)
    ser = None

def save_to_pkl(moisture, humidity, temperature, fertilizer):
    with open("data.pkl", "wb") as f:
        pickle.dump({
            "soilMoisture": round(moisture, 2),
            "humidity": round(humidity, 2),
            "temperature": round(temperature, 2),
            "fertilizer": fertilizer
        }, f)

def read_sensor_data():
    if not ser:
        print("Serial port not available.")
        return

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

        save_to_pkl(avg_moisture, avg_humidity, avg_temperature, predicted_fertilizer)
    else:
        print("No valid data received.")

# Schedule the function
schedule.every(10).seconds.do(read_sensor_data)

# Run scheduler in background
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask route for dashboard
@app.route('/')
def index():
    return render_template('index.html')  # HTML file should be inside a 'templates' folder

# Endpoint to return latest sensor data
@app.route('/get_data')
def get_data():
    try:
        with open("data.pkl", "rb") as f:
            data = pickle.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No data available"}), 404

if __name__ == '__main__':
    # Start the sensor scheduler in a separate thread
    thread = threading.Thread(target=run_schedule)
    thread.daemon = True
    thread.start()

    # Run the Flask app
    app.run(debug=True)
