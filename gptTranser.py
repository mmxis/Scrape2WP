import pandas as pd
import openai

# OPEN AI API Segment
api_key = 'Dein OopenAI API Key'
openai.api_key = api_key

# CSV-Datei laden die die gescrapten Artikel beinhaltet
csv_file = 'articles.csv'
df = pd.read_csv(csv_file)

# Funktion, um Text mithilfe der OpenAI API zusammenzufassen und zu übersetzen
def summarize_and_translate_text(text, source_language='en', target_language='de'):
    # Zusammenfassen
    summary_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please provide a similar version of the following text and make it plagiarism free: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    if summary_response.choices:
        summarized_text = summary_response.choices[0].text.strip()
    else:
        raise Exception('OpenAI API call failed')

    # Funktion zum Übersetzen der vorherigen Funktion
    translation_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from {source_language} to {target_language}: {summarized_text}, keep names,brands or organizations as it is in the original in the text.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    if translation_response.choices:
        translated_text = translation_response.choices[0].text.strip()
    else:
        raise Exception('OpenAI API call failed')

    return translated_text

# Funktion, um Text mithilfe der OpenAI API zusammenzufassen und zu übersetzen
def summarize_and_translate_title(text, source_language='en', target_language='de'):
    # Zusammenfassen
    summary_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please provide a similar version of the following text and make it plagiarism free: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    if summary_response.choices:
        summarized_text = summary_response.choices[0].text.strip()
    else:
        raise Exception('OpenAI API call failed')

    # Funktion zum Übersetzen der vorherigen Funktion
    translation_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from {source_language} to {target_language}: {summarized_text} keep names brands or organizations as it is in the original in the text.Make sure that the text fits good as a title on a news page and do not exceed 80 characters.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    if translation_response.choices:
        translated_text = translation_response.choices[0].text.strip()
    else:
        raise Exception('OpenAI API call failed')

    return translated_text

# Zusammenfassen und Übersetzen für jede Zeile in den gewählten Spalten
for idx, row in df.iterrows():
    # Für 'text' Spalte
    original_text = row['text']
    translated_summary_text = summarize_and_translate_text(original_text)
    df.at[idx, 'text'] = translated_summary_text

    # Für 'title' Spalte
    original_title = row['title']
    translated_summary_title = summarize_and_translate_title(original_title)
    df.at[idx, 'title'] = translated_summary_title

    print(f"Row {idx + 1}: Original Text = {original_text}")
    print(f"Row {idx + 1}: Translated Summary Text = {translated_summary_text}")
    print(f"Row {idx + 1}: Original Title = {original_title}")
    print(f"Row {idx + 1}: Translated Summary Title = {translated_summary_title}")
    print("\n")

# Ergebnis in einer neuen CSV-Datei speichern
output_csv_file = 'modified_csv_file.csv'
df.to_csv(output_csv_file, index=False)
print(f"Modified CSV file saved as {output_csv_file}")


