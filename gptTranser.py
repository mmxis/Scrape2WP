import openai

openai.api_key = "your_openai_api_key"

def rewrite_article(article):
    prompt = f"Bitte formuliere den folgenden Gaming-Artikel um: {article['title']} - {article['content']}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    rewritten_text = response.choices[0].text.strip()
    return rewritten_text

for article in scraped_articles:
    article['rewritten_content'] = rewrite_article(article)
