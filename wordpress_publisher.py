from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.media import UploadFile

def publish_to_wordpress(wp_client, article):
    # Bild hochladen
    image_data = requests.get(article['image_url']).content
    image_name = article['image_url'].split('/')[-1]

    media = {
        'name': image_name,
        'type': 'image/jpeg',
        'bits': image_data
    }

    image_id = wp_client.call(UploadFile(media))['id']

    # Artikel erstellen und veröffentlichen
    post = WordPressPost()
    post.title = article['title']
    post.content = article['rewritten_content']
    post.post_status = 'publish'
    post.thumbnail = image_id

    post_id = wp_client.call(NewPost(post))
    return post_id
