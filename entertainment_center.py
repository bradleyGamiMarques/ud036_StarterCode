import fresh_tomatoes
import media

#Create instances of our movie class 

back_to_the_future = media.Movie("Back To The Future",
                                  "Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                                  "https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=qvsgGtivCgs")

catch_me_if_you_can = media.Movie("Catch Me If You Can",
                                  "A seasoned FBI agent pursues Frank Abagnale Jr. who, before his 19th birthday, successfully forged millions of dollars' worth of checks while posing as a Pan Am pilot, a doctor, and a legal prosecutor.",
                                  "https://m.media-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_.jpg",
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")

forrest_gump = media.Movie("Forrest Gump",
                                  "The presidencies of Kennedy and Johnson, Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.",
                                  "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                                  "https://www.youtube.com/watch?v=bLvqoHBptjg")

full_metal_jacket = media.Movie("Full Metal Jacket",
                                  "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                                  "https://m.media-amazon.com/images/M/MV5BNzc2ZThkOGItZGY5YS00MDYwLTkyOTAtNDRmZWIwMGRhYTc0L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,656,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

inception = media.Movie("Inception",
                                  "A thief, who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                                  "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=YoHD9XEInc0")

se7en = media.Movie("Se7en",
                    "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.",
                    "https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,639,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=znmZoVkCjpI")

slumdog_millionaire = media.Movie("Slumdog Millionaire",
                                  "Love and money... You have mixed them both.",
                                  "https://m.media-amazon.com/images/M/MV5BZmNjZWI3NzktYWI1Mi00OTAyLWJkNTYtMzUwYTFlZDA0Y2UwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=JwiU94p9XPA")

the_prestige = media.Movie("The Prestige",
                                  "After a tragic accident two stage magicians engage in a battle to create the ultimate illusion whilst sacrificing everything they have to outwit the other.",
                                  "https://m.media-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg",
                                  "https://www.youtube.com/watch?v=ijXruSzfGEc")

the_princess_bride = media.Movie("The Princess Bride",
                                  "While home sick in bed, a young boy's grandfather reads him a story called The Princess Bride.",
                                  "https://m.media-amazon.com/images/M/MV5BMGM4M2Q5N2MtNThkZS00NTc1LTk1NTItNWEyZjJjNDRmNDk5XkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=WNNUcHRiPS8")

# Create a list of movie objects.
movies = [back_to_the_future, catch_me_if_you_can, forrest_gump, full_metal_jacket, inception, se7en, slumdog_millionaire, the_prestige, the_princess_bride]
# Call the open_movies_page function which takes in a list of movies.
fresh_tomatoes.open_movies_page(movies)
