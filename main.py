import argparse
import requests

import xml.etree.ElementTree as ET
import json

from models import Podcast, Episode



def request_rss(url_feed):
    response = requests.get(url_feed)
    return convert_xml_to_json(response.content, response.url)




def convert_xml_to_json(response_content, url_feed):
    try:
        tree = ET.XML(response_content)

        titulo = tree.find("./channel/title").text
        descricao = tree.find("./channel/description").text

        ultima_atualizacao =  tree.find("./channel/lastBuildDate").text

        thumb_img =  tree.find("./channel/image/url").text


        podcast = Podcast(titulo, ultima_atualizacao, url_feed, descricao, thumb_img)

        items_xml =  tree.findall('./channel/item')

        print(len(items_xml))

        for item in items_xml:
            titulo_episodio = item.find('./title').text
            link_site =  item.find('./link').text
            data_publicacao =  item.find('./pubDate').text

            guid_episodio =  item.find("./guid").text


            episodio =  Episode(titulo_episodio, data_publicacao, guid_episodio, link_site)

            podcast.add_episode(episodio)

        return podcast
    except Exception as e:
        print(e)

        


if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description="Converte o XML do RSS em JSON")
    parser.add_argument("--feed-rss", dest='feed_rss', action='store')

    args = parser.parse_args()

    feed_rss =  args.feed_rss

    json_rss = request_rss(feed_rss)

    with open("teste_feed.json", "w") as file:
        json.dump(json_rss.to_json(), file)
        


