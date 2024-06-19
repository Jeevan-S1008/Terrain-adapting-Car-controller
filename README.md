
# Terrain Detection using Azure Custom Vision

This project demonstrates terrain detection using Azure Custom Vision service. It classifies images into terrain types such as Sand and Mud Terrain, Snow and Wet, Ideal Condition, and Traffic, recommending appropriate driving modes based on the classification.

## Features

- **Image Classification:** Uses Azure Custom Vision to classify terrain types from images.
  
- **Mode Recommendation:** Recommends driving modes (OFFROAD, SNOW Mode, NORMAL mode, ECO mode) based on detected terrain.

## Setup

### Prerequisites

- Python 3.x
- Azure subscription with a Custom Vision resource

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Jeevan-S1008/Terrain-adapting-Car-controller.git
   cd terrain-detection
   ```
2. Open a new terminal window inside Visual Studio Code by selecting **Terminal** > **New Terminal Window**
 Create a new Python environment and install the packages by running the following command:

    ```bash
    # On Windows
    python3 -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt

    # On Linux, WSL or macOS
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. fill this 
     ```
     KEY=your_custom_vision_prediction_key
     ENDPOINT=your_custom_vision_endpoint_url
     PROJECT_ID=your_custom_vision_project_id
     PUBLISHED_ITERATION_NAME=your_published_iteration_name
     ```

### Usage

Run the script `main.py` to classify a test image located in `Testing images/t1.jpg`.

```
python main.py
```

The script will output the detected terrain type and recommend the appropriate driving mode based on the classification results.

If any queries reach out
