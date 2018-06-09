import webbrowser


class Movie():
    """ This class defines the characteristics of a movie.

        Attributes:
            attr1 (self): First parameter in the init function.
                attr2 (str): The title of the movie.
                attr3 (str): Brief description of the movie's story.
                attr4 (str): A URL to an image of the movie poster.
                attr5 (str): A URL to the movie's trailer on YouTube.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function opens a web browser which navigates to the passed in
        url.

                Attributes:
                attr1 (self): Allows us to access variables from the class.
        """

        # We pass in the URL as a string to this function that opens a
        # web browser.
        webbrowser.open(self.trailer_youtube_url)
