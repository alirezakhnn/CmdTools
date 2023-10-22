from translate import Translator

origin_lang = input("Enter your origin language: ")
dest_lang = input("Enter your destination language to translate: ")

def translate_text(text, dest=dest_lang, src=origin_lang):
    translator = Translator(to_lang=dest, from_lang=src)
    translation = translator.translate(text)
    return translation


# Example Usage:
if __name__ == "__main__":
    y='y'
    while y.lower() == 'y': 
        text_to_translate = input("Enter the text to be translated: ")
        translated_text = translate_text(text_to_translate)
        print("Translation => ", translated_text)
        y=input("do you want to retranslate? [y/n]: ")
        if(y == 'n'):
            break
    
