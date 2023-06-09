# Multi-Language Translation Tool
import os
from google.cloud import translate
from dotenv import load_dotenv
from languages import *
load_dotenv()

PROJECT_ID = str(os.getenv('PROJECT_ID'))
new_languages_list = []
codes = []
for language_option in language_list_dict:
    if language_option["status"] == True:
        language_to_translate = language_option["language"]
        language_code = language_option["code"]
        new_languages_list.append(language_to_translate)
        codes.append(language_code)

string_to_translate = input("Enter a string to translate: ")
print("String to be translated: ", string_to_translate)
output_language = ", ".join(new_languages_list)
print("Languages output: ", output_language)


def translate_text(text=string_to_translate, project_id=PROJECT_ID):
    OUTPUT_LANGUAGE_CODE = language_code_output
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": 'en-US',
            "target_language_code": OUTPUT_LANGUAGE_CODE,
        }
    )
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))


for language_code_output in output_language and codes:
    translate_text()
    print(language_code_output)
