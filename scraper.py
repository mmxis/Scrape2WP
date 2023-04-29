import newspaper
from newspaper import Article

url = "https://www.ign.com/articles/major-publishers-report-aaa-games-can-cost-over-a-billion-to-make"


article = Article(url)
article.download()
article.parse()

with open("article.txt", "w", encoding="utf-8") as f:
    f.write(article.title + "\n")
    # f.write("By " + ", ".join(article.authors) + "\n")
    # f.write(str(article.publish_date) + "\n")
    # f.write(article.summary) # works only with keyowrds to create a summary
    f.write(article.text)
