import webbrowser


class Movie():

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Movie object has been created
    # Movie will need to have 4 arguments in order to be created
    '''If Movie object was successful created than entertainment_center should
    have no errors'''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # If show_trailer is called a browser should open to the youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
