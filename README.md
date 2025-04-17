# AgriPredictor

AgriPredictor is a repository focused on predicting agricultural outcomes using advanced machine learning techniques. It aims to assist farmers and stakeholders in making data-driven decisions.

## Repository Link

[GitHub Repository](https://github.com/sakrish205/AgriPredictor)

## Features
- Crop yield prediction
- Weather analysis
- Soil quality assessment
- Data visualization tools

# Fertilizer Prediction System

## Description
The Fertilizer Prediction System is designed to analyze soil data and recommend fertilizers. It includes functionalities for data analysis, machine learning, and web-based interaction. This system aims to assist farmers in making data-driven decisions to improve crop yield and soil health.

## Features
- **Data Analysis**: Analyze soil data to extract meaningful insights.
- **Machine Learning**: Predict fertilizer requirements using trained models.
- **Web Interface**: User-friendly web interface for interaction.
- **Sensor Integration**: Support for soil moisture sensors and HTD22 sensors.

## Sensors Used
The system integrates soil moisture sensors and HTD22 sensors to measure soil moisture levels and environmental conditions like temperature and humidity. These sensors provide real-time data to ensure accurate fertilizer recommendations. Key features of the sensors include:
- High sensitivity and accuracy for detecting soil moisture levels.
- HTD22 sensor for temperature and humidity measurements.
- Easy integration with microcontrollers like Arduino and ESP32.

### Arduino Integration and ESP32 Pin Configuration

#### Arduino Code
The Arduino code for integrating soil moisture and HTD22 sensors is located in the `kasyyy/kasyyy.ino` file. This code is responsible for reading data from the sensors and transmitting it to the main application.

#### ESP32 Pin Configuration
To connect the soil moisture and HTD22 sensors to an ESP32 microcontroller, use the following pin configuration:

| Sensor Pin       | ESP32 Pin | Description                     |
|------------------|-----------|---------------------------------|
| Soil Moisture VCC| 3.3V      | Power supply for soil sensor    |
| Soil Moisture GND| GND       | Ground for soil sensor          |
| Soil Moisture OUT| GPIO32    | Analog output for soil moisture |
| HTD22 VCC        | 3.3V      | Power supply for HTD22 sensor   |
| HTD22 GND        | GND       | Ground for HTD22 sensor         |
| HTD22 DATA       | GPIO33    | Data pin for HTD22 sensor       |

Ensure that the ESP32 is properly powered and that the connections are secure. For more details, refer to the Arduino code and the sensor's datasheet.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PALS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PALS
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the project, execute the following command:
```bash
python app.py
```

### Web Interface
1. Open your browser and navigate to `http://127.0.0.1:5000` after running the app.
2. Use the interface to upload soil data and get fertilizer recommendations.

### Arduino Integration
Refer to the `kasyyy/kasyyy.ino` file for Arduino code to integrate soil moisture and HTD22 sensors.

## Project Structure
```
PALS/
├── aaa.py
├── app.py
├── best_rf_model.pkl
├── Collab.url
├── Complete-Guide-for-NPK-Soil-Sensor-with-Arduino-Tutorial.jpg
├── data_core.csv
├── data.pkl
├── fertilizer_encoding.pkl
├── README.md
├── requirements.txt
├── arduino/
│   └── arduino.ino
├── templates/
│   └── index.html
```

## Requirements
The project requires the Python packages listed in `requirements.txt`.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Open-source libraries and tools used in this project.