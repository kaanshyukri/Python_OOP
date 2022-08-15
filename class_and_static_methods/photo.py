from math import ceil


class PhotoAlbum:
    PHOTO_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTO_PER_PAGE)
        return cls(pages)

    def build_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTO_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        result = separator
        for page in self.photos:
            result += ' '.join("[]" for _ in page) + "\n"
            result += separator
        return result.strip()



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
