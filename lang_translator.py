import sys
import json
from watson_developer_cloud import LanguageTranslatorV2

language_translator = LanguageTranslatorV2(
    username='5c50c1a2-eef6-4d52-9453-b24aa3d6e35e',
    password='X1eIoqJZnlL8')

args = sys.argv

text = args[1]
src = args[2]
dest = args[3]

print(json.dumps(language_translator.translate(text, source=src, target=dest), indent=2, ensure_ascii=False))