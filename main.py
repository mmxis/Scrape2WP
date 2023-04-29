from scraper import scrape_articles
from rewriter import rewrite_article
from wordpress_publisher import publish_to_wordpress
from wordpress_xmlrpc import Client

news_url = "https://example-gaming-news-site.com"
scraped_articles = scrape_articles(news_url)

# Artikel umformulieren
for article in scraped_articles:
    article['rewritten_content'] = rewrite_article(article)

# Artikel auf der WordPress-Seite veröffentlichen
wp_url = "https://your-wordpress-site.com/xmlrpc.php"
wp
