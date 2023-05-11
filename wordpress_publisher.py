import pandas as pd
import requests
import json
import base64
import datetime
import ssl
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# SSL-Zertifikatsüberprüfung deaktivieren (Nur für Testzwecke)
ssl._create_default_https_context = ssl._create_unverified_context

# Ersetzen Sie diese Informationen mit Ihren WordPress-Anmeldedaten
wp_url = "https://gameologen.de/xmlrpc.php"
wp_username = "username"
wp_password = "password"

# CSV-Datei laden
csv_file = 'modified_csv_file.csv'
df = pd.read_csv(csv_file)

# WordPress-Client erstellen
client = Client(wp_url, wp_username, wp_password)

# Artikel aus der CSV-Datei auf der WordPress-Seite hochladen
for idx, row in df.iterrows():
    post = WordPressPost()
    post.title = row['title']
    post.content = row['text']
    #post.date = row['date']  # Stellen Sie sicher, dass die Spalte 'date' in der CSV-Datei vorhanden ist
    post.post_status = 'publish'
    post.author = 'your_author_id'  # Ersetzen Sie 'your_author_id' durch die ID Ihres Autors

    if pd.isna(row['date']):
        print(f"Row {idx + 1}: Invalid date value. Using current date as default.")
        post.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        post.date = row['date']

    # Optional: Fügen Sie Kategorien und Tags hinzu
    # post.terms_names = {
    #     'category': ['Category 1', 'Category 2'],
    #     'post_tag': ['Tag 1', 'Tag 2'],
    # }

    try:
        post_id = client.call(NewPost(post))
        print(f"Row {idx + 1}: Article uploaded with post ID = {post_id}")
    except ValueError as e:
        print(f"Row {idx + 1}: Error uploading article - {e}")

    post_id = client.call(NewPost(post))
    print(f"Row {idx + 1}: Article uploaded with post ID = {post_id}")
