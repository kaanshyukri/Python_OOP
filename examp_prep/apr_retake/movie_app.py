from test_apr_retake import User
from test_apr_retake import Movie


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_username(self, username):
        for user in self.users_collection:
            if username == user.username:
                return True
        return False

    def find_movie(self, movie):
        if movie in self.movies_collection:
            return True
        return False

    def register_user(self, username, age):
        if self.find_username(username):
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        if self.find_movie(movie):
            raise Exception("Movie already added to the collection!")

        if not self.find_username(username):
            raise Exception("This user does not exist!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
                return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie: Movie, **kwargs):

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if not self.find_movie(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie: Movie):

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if not self.find_movie(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.movies_collection.pop(self.movies_collection.index(movie))
        for user in self.users_collection:
            if username == user.username:
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie: Movie):

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        for user in self.users_collection:
            if username == user.username:
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
                user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie: Movie):
        for user in self.users_collection:
            if username == user.username:
                if movie not in user.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")
                user.movies_liked.pop(user.movies_liked.index(movie))
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        result = ""
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            users = []
            for user in self.users_collection:
                users.append(user.username)
            result += f"All users: {', '.join(users)}\n"

        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            titles = []
            for movie in self.movies_collection:
                titles.append(movie.title)
            result += f"All movies: {', '.join(titles)}"
        return result

