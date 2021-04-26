#you will need the following library 
!pip install ibm_watson wget

# import the appropriate libraries
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# load the URL and API key for the speech to text cloud instance
url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/70094984-dda6-44ef-8eaa-a7546f96c741"
iam_apikey_s2t = "2NEesa7CW3Tz2kb-NLpYIieOjgDSlU_jXJX0QDbEBAQi"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# this calls an MP3 file with the appropriate speech
!wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

# Path of the MP3 file
filename='PolynomialRegressionandPipelines.mp3'

# Create the file object with the wav file using open, set the mode to rb which reads in binary

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
#response.result

# Use pandas to normalize the text
from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
