import fresh_tomatoes
import media

#Create instances of our movie class 

full_metal_jacket = media.Movie("Full Metal Jacket",
                                  "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                                  "https://m.media-amazon.com/images/M/MV5BNzc2ZThkOGItZGY5YS00MDYwLTkyOTAtNDRmZWIwMGRhYTc0L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,656,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

slumdog_millionaire = media.Movie("Slumdog Millionaire",
                                  "Love and money... You have mixed them both.",
                                  "https://m.media-amazon.com/images/M/MV5BZmNjZWI3NzktYWI1Mi00OTAyLWJkNTYtMzUwYTFlZDA0Y2UwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=JwiU94p9XPA")

the_prestige = media.Movie("The Prestige",
                                  "After a tragic accident two stage magicians engage in a battle to create the ultimate illusion whilst sacrificing everything they have to outwit the other.",
                                  "https://m.media-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg",
                                  "https://www.youtube.com/watch?v=ijXruSzfGEc")
movies = [full_metal_jacket, slumdog_millionaire, the_prestige]
fresh_tomatoes.open_movies_page(movies)
