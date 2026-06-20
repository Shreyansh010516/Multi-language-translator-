from deep_translator import GoogleTranslator

print("MULTI LANGUAGE TRANSLATOR")

text = input("Enter Text: ")

target_language = input("Enter Target Language: ").lower()

translated_text = GoogleTranslator(
    source="auto",
    target=target_language
).translate(text)

print("\nTranslated Text:")
print(translated_text)
