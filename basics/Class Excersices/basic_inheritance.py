class CGI:
    def __init__(self):
        super(CGI, self).__init__()
        self.type = '';

    def set_cgi_type(self, type):
        self.type = type;



class Manga:
    def __init__(self):
        super(Manga, self).__init__()
        self.title = 'N/A'

    def add_manga_source(self, title):
        self.title = title


class Anime(CGI, Manga):
    def __init__(self):
        super(Anime, self).__init__()
        self.name = '';
        self.genre = '';
    
    def set_values(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return (' Inspired By: ' + self.title + '\n Title: ' +self.name +'\n Genre: ' + self.genre)

ajin = Anime()
ajin.set_values('Ajin - DemiHumans', 'Seinen')
ajin.set_cgi_type('Battle CGI')
ajin.add_manga_source('Ajin')

print(ajin)
