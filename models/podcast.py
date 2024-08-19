class Podcast:
    def __init__(self, nome, data_atualizacao, link_feed, descricao, thumb_img) -> None:
        self.nome = nome
        self.data_atualizacao = data_atualizacao
        self.link_feed = link_feed
        self.descricao = descricao

        self.thumb_img = thumb_img
        self.episodes = []


    def add_episode(self,episode):
        self.episodes.append(episode)



    def to_json(self):
        return {
            "nome": self.nome,
            "link_feed": self.link_feed,
            "descricao": self.descricao,
            "thumb_img": self.thumb_img,
            "episodes": [ episode.to_json() for episode in self.episodes ]
        }

    
