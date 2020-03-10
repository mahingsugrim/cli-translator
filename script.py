import sys
from translate import Translator

sys.argv

# text to be translated
text = sys.argv[1]

# language into which text will be converted
lang = sys.argv[2]
translator = Translator(to_lang = lang)

translation = translator.translate(text)
print(translation)
