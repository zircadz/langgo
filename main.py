# Multi-Language Translation Tool
import os
from google.cloud import translate
from dotenv import load_dotenv
from languages import *
load_dotenv()

PROJECT_ID = str(os.getenv('PROJECT_ID'))
newlist = sorted(language_list)
newlanguages = []
codes = []
for c in language_list_dict:
    if c["status"] == True:
        language_to_translate = c["language"]
        language_code = c["code"]
        newlanguages.append(language_to_translate)
        codes.append(language_code)

input_string = input("Enter a string to translate: ")
print("Word to be translated: ", input_string)
output_language = newlanguages
print(output_language)


# HERE IS WHERE WE NEED TO RUN THE LANGUAGE CODE THROUGH THE NEXT FUNCTION

def translate_text(text=input_string, project_id=PROJECT_ID):
    OUTPUT_LANGUAGE = i
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": 'en-US',
            "target_language_code": OUTPUT_LANGUAGE,
        }
    )
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))


for i in output_language and codes:
    translate_text()
    print(i)
