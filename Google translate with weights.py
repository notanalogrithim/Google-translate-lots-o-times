import time
import random
from deep_translator import GoogleTranslator

# Code comments are for the weak 
random.seed(123)
tenComandments = """
1. לֹא יִהְיֶה לְךָ אֱלֹהִים אֲחֵרִים עַל פָּנָי.
2. לֹא תַעֲשֶׂה לְךָ פֶּסֶל וְכָל תְּמוּנָה.
3. לֹא תִשָּׂא אֶת שֵׁם־יְהוָה אֱלֹהֶיךָ לַשָּׁוְא.
4. זָכוֹר אֶת־יוֹם הַשַּׁבָּת לְקַדְּשׁוֹ.
5. כַּבֵּד אֶת־אָבִיךָ וְאֶת־אִמֶּךָ.
6. לֹא תִרְצָח.
7. לֹא תִנְאָף.
8. לֹא תִגְנֹב.
9. לֹא תַעֲנֶה בְרֵעֲךָ עֵד שָׁקֶר.
10. לֹא תַחְמֹד.
"""

text = tenComandments
#text = input("What text would you like to translate? ")
def weighted_random_choice(languages, weights):
    return random.choices(languages, weights=weights, k=1)[0]

supported_languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 
    'ny', 'zh-CN', 'zh-TW', 'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl', 'fi', 
    'fr', 'fy', 'gl', 'ka', 'da', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 
    'ilo', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 'lo', 
    'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mni-Mtei', 'lus', 
    'mn', 'my', 'ne', 'no', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 
    'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 
    'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]

weights = {
    'af': 1, 'sq': 2, 'am': 3, 'ar': 5, 'hy': 5, 'as': 2, 'ay': 7, 'az': 3, 'bm': 6, 'eu': 4, 'be': 4, 'bn': 3,
    'bho': 7, 'bs': 2, 'bg': 3, 'ca': 2, 'ceb': 4, 'ny': 7, 'zh-CN': 10, 'zh-TW': 10, 'co': 6, 'hr': 3, 'cs': 3,
    'da': 2, 'dv': 6, 'doi': 7, 'nl': 2, 'en': 1, 'eo': 3, 'et': 4, 'ee': 6, 'tl': 5, 'fi': 4, 'fr': 2, 'fy': 5,
    'gl': 3, 'ka': 5, 'el': 4, 'gn': 7, 'gu': 4, 'ht': 6, 'ha': 6, 'haw': 5, 'iw': 5, 'hi': 4, 'hmn': 7, 'hu': 5,
    'is': 6, 'ig': 7, 'ilo': 6, 'id': 2, 'ga': 5, 'it': 2, 'ja': 10, 'jw': 7, 'kn': 6, 'kk': 5, 'km': 7, 'rw': 6,
    'gom': 7, 'ko': 6, 'kri': 7, 'ku': 5, 'ckb': 6, 'ky': 5, 'lo': 6, 'la': 6, 'lv': 4, 'ln': 7, 'lt': 4, 'lg': 7,
    'lb': 5, 'mk': 4, 'mai': 7, 'mg': 6, 'ms': 4, 'ml': 5, 'mt': 5, 'mi': 7, 'mr': 5, 'mni-Mtei': 7, 'lus': 7,
    'mn': 6, 'my': 6, 'ne': 4, 'no': 2, 'or': 6, 'om': 7, 'ps': 6, 'fa': 5, 'pl': 3, 'pt': 2, 'pa': 5, 'qu': 7,
    'ro': 3, 'ru': 5, 'sm': 7, 'sa': 6, 'gd': 6, 'nso': 7, 'sr': 5, 'st': 7, 'sn': 7, 'sd': 6, 'si': 6, 'sk': 4,
    'sl': 4, 'so': 6, 'es': 2, 'su': 7, 'sw': 6, 'sv': 2, 'tg': 6, 'ta': 5, 'tt': 7, 'te': 5, 'th': 6, 'ti': 7,
    'ts': 7, 'tr': 5, 'tk': 6, 'ak': 7, 'uk': 5, 'ur': 5, 'ug': 7, 'uz': 5, 'vi': 3, 'cy': 7, 'xh': 7, 'yi': 7,
    'yo': 6, 'zu': 6
}

x = input("How many times would you like to translate the text? ")
for i in range(x):
    try:
        lang = weighted_random_choice(supported_languages, [weights[lang] for lang in supported_languages])
        text = GoogleTranslator(source='auto', target=lang).translate(text)
        print(f"Step {i+1}: Translated to {lang}")
    except Exception as e:
        print(f"Error during translation at step {i}: {e}")
        continue 

try:
    final_text = GoogleTranslator(source='auto', target='en').translate(text)
    print("Final translated text back to English:")
    print(final_text)
except Exception as e:
    print(f"Error translating back to English: {e}")
