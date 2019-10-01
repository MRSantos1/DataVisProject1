# Import Dependencies
import pandas as pd

# Initialize data of lists based on previous data extraction
movie_data = {'Movie Name' : ['Focus', 'Termintor Genisys', 'Pan', 'Ted 2', 'Inside Out',
'Goosebumps', 'Aloha', 'Cinderella', 'Self/less', 'Ip Man 3', '13 Hours',
'Ghostbusters', 'My Big Fat Greek Wedding 2', 'Gods of Egypt', 'Eddie the Eagle',
'Star Trek Beyond', 'London Has Fallen', 'The 5th Wave', 'Suicide Squad', 'Me Before You'],
'IMDB Rating' : [66, 64, 57, 63, 82, 63, 54, 69, 65, 71, 73, 78, 60, 54, 74, 71, 59, 52, 60, 74],
'Rotten Tomatoes Rating' : [56, 26, 27, 45, 98, 78, 20, 85, 19, 78, 51, 97, 28, 16, 82, 86, 26, 15, 27, 55],
'Metacritic Rating' : [56, 38, 36, 48, 94, 60, 40, 67, 34, 57, 48, 71, 37, 25, 54, 68, 28, 33, 40, 51],
'Facebook Likes' : [23000, 82000, 24000, 30000, 118000, 35000, 11000, 56000, 11000, 12000,
                    44000, 62000, 19000, 24000, 15000, 30000, 28000, 14000, 80000, 51000]}

# Create the DataFrame
master_movie_df = pd.DataFrame(movie_data)

# Print DataFrame
master_movie_df