
class Entertainment:
    def __init__(self, name ):
        self.name = name
        # self.type = type

    def display(self):
        print(f"Type of entertainment : {self.name}")

class Movie(Entertainment):
    def __init__(self, name, type):
       self.name = name
       self.type = type
       print(f"Type of movie : {self.type}")

class Books(Entertainment):
    def __init__(self, name, author):
        # super().__init__(name)
        self.name = name
        self.author = author
        print(f"author : {self.author}")

class Music(Entertainment):
    def __init__(self, name, music_name):
        # super().__init__(name)
        self.name = name
        self.music_name = music_name
        print(f"Music name : {self.music_name}")

class Rock(Music):
    def __init__(self, name, music_name, type):
        Music.__init__(self,name, music_name)
        self.name = name
        self.music_name = music_name
        self.type = type
        print(f"Music type : {self.type}")

class Pop(Music):
    def __init__(self, name, music_name, type):
        Music.__init__(self, name, music_name)
        self.type = type
        print(f"Music type : {self.type}")

movie = Movie("harry potter", "horror")
movie.display()

book = Books("Psycho Software","Thoe Saung")
book.display()

rock = Rock("Music", "Blank Space", "pop")
rock.display()

pop = Pop("Music", "Hello", "pop")
pop.display()




