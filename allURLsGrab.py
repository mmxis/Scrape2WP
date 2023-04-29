import newspaper
from newspaper import Article
import pandas as pd

ign_url = 'https://www.ign.com/news'
ign = newspaper.build(ign_url, memoize_articles=False)

num_articles = min(3, len(ign.articles))

# Leere Liste wird erstellt um die Artikel Infos zu speichern
articles_data = []

for i in range(num_articles):
    article = ign.articles[i]
    article.download()
    article.parse()
    print(f"Article {i + 1}: {article.title,article.url}")

    # Artikelinfos werden in einer Dictionary gespeichert (später für die CSV)
    article_info = {
        "title": article.title,
        "text": article.text,
        "date": article.publish_date
    }

    # Dictionary wird zur Liste der Artikelinformationen hinzugefügt
    articles_data.append(article_info)

# Erstellen des pandas DataFrame aus der Liste der Artikelinformationen
df = pd.DataFrame(articles_data)

# Speichern des DataFrames als CSV-Datei
df.to_csv("articles.csv", index=False)
