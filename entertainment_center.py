import fresh_tomatoes
import media

# Create instances of our movie class.

back_to_the_future = media.Movie("Back To The Future", """Marty McFly,
a 17-year-old high school student, is accidentally sent thirty years into the
past in a time-traveling DeLorean invented by his
close friend, the maverick scientist Doc Brown.""",
                                 "https://bit.ly/2JtWnOj",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

catch_me_if_you_can = media.Movie(
    "Catch Me If You Can",
    """A seasoned FBI
agent pursues Frank Abagnale Jr. who, before his 19th birthday,
successfully forged millions of dollars' worth of checks while posing as a Pan
Am pilot, a doctor, and a legal prosecutor.""",
    "https://bit.ly/2sLcocg",
    "https://www.youtube.com/watch?v=71rDQ7z4eFg")

forrest_gump = media.Movie("Forrest Gump", """The presidencies of Kennedy and
Johnson, Vietnam, Watergate, and other history unfold through the perspective
of an Alabama man with an IQ of 75.""",
                           "https://bit.ly/2HxYoY8",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

full_metal_jacket = media.Movie("Full Metal Jacket", """A pragmatic U.S.
Marine observes the dehumanizing effects the Vietnam War has on his fellow
recruits from their brutal boot camp training to the bloody street fighting in
Hue.""",
                                "https://bit.ly/2JuD8Eh",
                                "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

inception = media.Movie("Inception", """A thief, who steals corporate secrets
through the use of dream-sharing technology, is given the inverse task of
planting an idea into the mind of a CEO.""",
                        "https://bit.ly/2JoFQPM",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

se7en = media.Movie("Se7en", """Two detectives, a rookie and a veteran, hunt
a serial killer who uses the seven deadly sins as his motives.""",
                    "https://bit.ly/2kZBfVt",
                    "https://www.youtube.com/watch?v=znmZoVkCjpI")

slumdog_millionaire = media.Movie(
    "Slumdog Millionaire",
    "Love and money... You have mixed them both.",
    "https://bit.ly/2sU77Pb",
    "https://www.youtube.com/watch?v=JwiU94p9XPA")

the_prestige = media.Movie("The Prestige", """After a tragic accident two stage
magicians engage in a battle to create the ultimate illusion whilst
sacrificing everything they have to outwit the other.""",
                           "https://bit.ly/2kYGxAB",
                           "https://www.youtube.com/watch?v=ijXruSzfGEc")

the_princess_bride = media.Movie(
    "The Princess Bride",
    """While home sick in bed, a young boy's grandfather reads him a story called
 The Princess Bride.""",
    "https://bit.ly/2HBVdhZ",
    "https://www.youtube.com/watch?v=WNNUcHRiPS8")

# Create a list of movie objects.
movies = [back_to_the_future, catch_me_if_you_can, forrest_gump,
          full_metal_jacket, inception, se7en, slumdog_millionaire,
          the_prestige, the_princess_bride]

# Call the open_movies_page function which takes in a list of movies.
fresh_tomatoes.open_movies_page(movies)
