from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv
import os

# Load the key and endpoint values from the .env file
load_dotenv()

# Set the values into variables
key = os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
project_id = os.getenv('PROJECT_ID')
published_name = os.getenv('PUBLISHED_ITERATION_NAME')

if not key or not endpoint or not project_id or not published_name:
    raise ValueError("One or more environment variables are missing.")

# Setup credentials for client
credentials = ApiKeyCredentials(in_headers={'Prediction-key': key})

# Create client, which will be used to make predictions
client = CustomVisionPredictionClient(endpoint, credentials)

# Correct the file path
image_path = r'C:\Users\Katana\Desktop\MiniPro\Testing images\t1.jpg'  # Use raw string to avoid escape character issues

# Open the test file
with open(image_path, 'rb') as image:
    # Perform the prediction
    results = client.classify_image(project_id, published_name, image.read())

    # Because there could be multiple predictions, we loop through each one
    for prediction in results.predictions:
        # Display the name of the breed, and the probability percentage
        print(f'{prediction.tag_name}: {prediction.probability:.2%}')

max_prediction = max(results.predictions, key=lambda p: p.probability)

highest_prob_tag = max_prediction.tag_name
highest_prob_value = max_prediction.probability
 
if highest_prob_tag == 'Sand and Mud Terrain':
    print(f'Highest Probability Prediction: {highest_prob_tag} with a probability of {highest_prob_value:.2%} so switching to OFFROAD mode')
elif highest_prob_tag == 'Snow and Wet':
    print(f'Highest Probability Prediction: {highest_prob_tag} with a probability of {highest_prob_value:.2%} so switching to SNOW Mode')
elif highest_prob_tag == 'Ideal Condition':
    print(f'Highest Probability Prediction: {highest_prob_tag} with a probability of {highest_prob_value:.2%} so switching to NORMAL mode')
elif highest_prob_tag == 'Traffic':
    print(f'Highest Probability Prediction: {highest_prob_tag} with a probability of {highest_prob_value:.2%} so switching to ECO mode')
else:
    print("Couldn't Detect, Please use your driving skills")