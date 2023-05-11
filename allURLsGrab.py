import newspaper
from newspaper import Article
import pandas as pd


ign_url = 'https://kotaku.com/culture/news'
ign = newspaper.build(ign_url, memoize_articles=False)

# Amount of Scraped Articles (default is 20 because of outOfIndex)
num_articles = min(2, len(ign.articles))

# Leere Liste wird erstellt um die Artikel Infos zu speichern
articles_data = []

for i in range(num_articles):
    article = ign.articles[i]
    article.download()
    article.parse()
    print(f"Article {i + 1}: {article.title,article.url}")

    # Datum im Format "YYYY-MM-DD HH:MM:SS" (WordPress gemäß) konvertieren.
    publish_date_str = None
    if article.publish_date:
        #publish_date_str = article.publish_date.strftime("%Y-%m-%d %H:%M:%S")
        year = article.publish_date.year
        month = article.publish_date.month
        day = article.publish_date.day
        hour = article.publish_date.hour
        minute = article.publish_date.minute
        second = article.publish_date.second
        publish_date_str = f"{year:04d}-{month:02d}-{day:02d}  {hour:02d}:{minute:02d}:{second:02d}"


    # Artikelinfos werden in einer Dictionary gespeichert (später für die CSV)
    article_info = {
        "title": article.title,
        "text": article.text,
        "date": publish_date_str
    }

    # Dictionary wird zur Liste der Artikelinformationen hinzugefügt
    articles_data.append(article_info)

# Erstellen des pandas DataFrame aus der Liste der Artikelinformationen
df = pd.DataFrame(articles_data)

# Speichern des DataFrames als CSV-Datei
df.to_csv("articles.csv", index=False)
