import media
from movies import fresh_tomatoes

#A list of Movie with the attributes
# movie_title, movie_storyline, poster_image, trailer_youtube
departed = media.Movie("The Departed", "A corrupt cop and an undercover cop",
                       "http://www.gstatic.com/tv/thumb/movieposters"
                       "/162564/p162564_p_v8_ag.jpg",
                       "https://www.youtube.com/watch?v=iojhqm0JTW4")

inception = media.Movie("Inception", "A dream within a dream",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcR"
                        "o9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

batman = media.Movie("The Dark Knight",
                     "A guy who roams the city at night fighting crime",
                     "http://keyassets-p2.timeincuk.net/wp/prod/wp-content/"
                     "uploads/sites/42/2009/01/dark-knight-imax-337x500.jpg",
                     "https://www.youtube.com/watch?v=kmJLuwP3MbY")

fightclub = media.Movie("Fight Club", "A guy"
                        "who creates a club for people to fight one another",
                        "http://www.gstatic.com/tv/thumb/"
                        "movieposters/23069/p23069_p_v8_ad.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

goodwillhunting = media.Movie("Good Will Hunting",
                              "A janitor who is super smart,"
                              " but had a rough upbringing",
                              "http://t0.gstatic.com/images?q=tbn:ANd9GcT4vHOL"
                              "WBM56R6fNs7K9xcEf7V8M8mzrzi6LtWGXrqfg8-KynGn",
                              "https://www.youtube.com/watch?v=PaZVjZEFkRs")

thetown = media.Movie("The Town",
                      "A bunch of bank robbers doing the dirty "
                      "work of the Boston Mafia",
                      "http://t0.gstatic.com/images?q=tbn:"
                      "ANd9GcSrNPX7jG0kC3j9lUO1hrw-"
                      "7S-QJWZYeHGmUF5Nw8vXv7rZE5ac",
                      "https://www.youtube.com/watch?v=WcXt9aUMbBk")

startrek2009 = media.Movie("Star Trek", "Fighting in outer space",
                           "http://img.goldposter.com/2016/01/"
                           "Star-Trek_poster_goldposter_com_43.jpg",
                           "https://www.youtube.com/watch?v=pKFUZ10Wmbw")

fivehundreddaysofsummer = media.Movie("500 Days of Summer",
                                      "A story of a boy meets girl",
                                      "http://www.gstatic.com/tv/thumb/mo"
                                      "vieposters/193428/p193428_p_v8_av.jpg",
                                      "https://www.youtube.com/watch?v="
                                      "PsD0NpFSADM")

pitchperfect = media.Movie("Pitch Perfect",
                           "A girl joins an a cappella group",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcT1au"
                           "KQEhoF6KOJ_wXKHtvGoOV91-6iv8Nu367yAZMWcyWpvZKY",
                           "https://www.youtube.com/watch?v=PsD0NpFSADM")

ipman = media.Movie("IP Man",
                    "A martial artist who fought to provide for his family",
                    "http://www.gstatic.com/tv/thumb/movieposters/"
                    "3586588/p3586588_p_v8_ac.jpg",
                    "https://www.youtube.com/watch?v=1AJxXQ7xojE")

#Every movie is put into a list
movies = [departed, inception, batman, fightclub, goodwillhunting, thetown,
          startrek2009, fivehundreddaysofsummer, pitchperfect, ipman]

#fresh_tomatoes.py will open a local web page containing the list of movies
#Movie title and poster of the specific movie will be shown
fresh_tomatoes.open_movies_page(movies)
