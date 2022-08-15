from classes_and_objects.exercise.spoopify.album import Album
from classes_and_objects.exercise.spoopify.song import Song

class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album_name == album.name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()
        return result


song = Song("Scavenger of human sorrow", 6.56, False)
album = Album("The sound of perseverance")

# print(song.get_info())
# second_song = Song("Around the World", 2.34, False)
album.add_song(song)
print(album.remove_song("Scavenger of human sorrow"))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
