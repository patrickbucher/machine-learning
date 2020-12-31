The training data (`movies_content.csv`) contains 15 movies rated by 6 users.
The two right-most columns indicate the genre (Action, Romance) of the movie.

                         Movie  Alice  Bob  Carol  Dave  Erica  Frank  Action  Romance
    0                  Titanic    4.5  2.5    5.0   2.0    4.5    1.5     3.0      4.5
    1        Lord of the Rings    1.5  4.5    2.5   4.0    1.0    5.0     4.5      1.5
    2            The Godfather    3.5  4.5    3.0   5.0    4.0    5.0     4.5      3.5
    3                  Vertigo    4.5  3.5    4.0   4.0    5.0    4.0     3.0      4.0
    4              Rear Window    1.5  5.0    2.0   4.5    2.0    5.0     4.5      1.5
    5       Brokeback Mountain    5.0  1.0    5.0   1.0    5.0    1.0     1.0      5.0
    6         Dawn of the Dead    1.0  5.0    1.0   5.0    1.0    4.5     5.0      1.5
    7            Hateful Eight    1.5  4.5    2.0   5.0    2.5    4.5     4.5      1.5
    8             Pulp Fiction    2.0  4.5    1.5   5.0    1.5    5.0     4.5      1.5
    9   Breakfast at Tiffany's    5.0  1.0    5.0   1.0    5.0    1.0     1.0      5.0
    10            Notting Hill    NaN  NaN    5.0   2.0    5.0    1.5     1.0      5.0
    11                   Speed    3.5  5.0    NaN   NaN    2.5    4.5     5.0      3.0
    12           Jurassic Park    1.5  4.5    2.0   4.0    NaN    NaN     4.5      1.5
    13       Prince of Zamunda    NaN  NaN    NaN   NaN    NaN    NaN     1.5      4.5
    14               The Joker    NaN  NaN    NaN   NaN    NaN    NaN     4.0      2.0
    15                Downfall    NaN  NaN    NaN   NaN    NaN    NaN     4.5      3.5

The model is trained using the genre indications:

    cost =  115.170
    cost =   31.796
    cost =   16.691
    cost =   11.150
    cost =    9.088
    cost =    8.313
    cost =    8.019
    cost =    7.906
    cost =    7.863
    cost =    7.846

The trained model is then used to fill in the missing ratings:

                         Movie  Alice  Bob  Carol  Dave  Erica  Frank  Action  Romance
    0                  Titanic    4.5  3.0    4.5   3.0    4.5    3.0     3.0      4.5
    1        Lord of the Rings    1.5  4.5    1.5   4.5    1.5    4.5     4.5      1.5
    2            The Godfather    3.5  4.5    3.5   4.5    3.5    4.5     4.5      3.5
    3                  Vertigo    4.0  3.0    4.0   3.0    4.0    3.0     3.0      4.0
    4              Rear Window    1.5  4.5    1.5   4.5    1.5    4.5     4.5      1.5
    5       Brokeback Mountain    5.0  1.0    5.0   1.5    5.0    1.0     1.0      5.0
    6         Dawn of the Dead    1.5  5.0    2.0   5.0    1.5    5.0     5.0      1.5
    7            Hateful Eight    1.5  4.5    1.5   4.5    1.5    4.5     4.5      1.5
    8             Pulp Fiction    1.5  4.5    1.5   4.5    1.5    4.5     4.5      1.5
    9   Breakfast at Tiffany's    5.0  1.0    5.0   1.5    5.0    1.0     1.0      5.0
    10            Notting Hill    5.0  1.0    5.0   1.5    5.0    1.0     1.0      5.0
    11                   Speed    3.0  5.0    3.0   5.0    3.0    5.0     5.0      3.0
    12           Jurassic Park    1.5  4.5    1.5   4.5    1.5    4.5     4.5      1.5
    13       Prince of Zamunda    4.5  1.5    4.5   1.5    4.5    1.5     1.5      4.5
    14               The Joker    2.0  4.0    2.0   4.0    2.0    4.0     4.0      2.0
    15                Downfall    3.5  4.5    3.5   4.5    3.5    4.5     4.5      3.5

