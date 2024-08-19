import json

class Episode:
    def __init__(self, title, publish_date, guid, link_site):
        self.title = title
        self.publish_date = publish_date
        self.guid =  guid
        self.link_site =  link_site


    def to_json(self):
        return {
            "title": self.title,
            "publish_date": self.publish_date,
            "guid": self.guid,
            "link_site": self.link_site
        }

    


