#Real World Data sourced from the Web - URL: 'https://www.kaggle.com/justinas/nba-players-data'
#The data includes NBA Players covering the playing seasons from 1996 to 2020.

import pandas as pd
df = pd.read_csv(r"C:\Users\Lessa\1. UCD-NBA Project\all_seasons.csv")

#Import Numpy, Matplotlib and Seaborn:
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#ANALYZING DATA
#To check the first 5 rows and also the size of the dataset:
#print(df.head())
#Returned:
#Unnamed: 0        player_name team_abbreviation  ...  ts_pct  ast_pct   season
#0           0      Dennis Rodman               CHI  ...   0.479    0.113  1996-97
#1           1  Dwayne Schintzius               LAC  ...   0.430    0.048  1996-97
#2           2       Earl Cureton               TOR  ...   0.376    0.148  1996-97
#3           3        Ed O'Bannon               DAL  ...   0.399    0.077  1996-97
#4           4        Ed Pinckney               MIA  ...   0.611    0.040  1996-97
#
#[5 rows x 22 columns]
#
#Process finished with exit code 0
#
#To check to last 5 rows of the dataset - to see the number of the last few rows:
#print(df.tail())
#Returned:
#Unnamed: 0         player_name  ... ast_pct   season
#11140       11140         Maxi Kleber  ...   0.064  2019-20
#11141       11141  Melvin Frazier Jr.  ...   0.033  2019-20
#11142       11142      Meyers Leonard  ...   0.076  2019-20
#11143       11143        Norvel Pelle  ...   0.056  2019-20
#11144       11144         Matt Thomas  ...   0.089  2019-20
#
#[5 rows x 22 columns]
#
#Process finished with exit code 0
#
#To check how many rows and columns are in the dataset:
#print(df.shape)
#Returned:
#(11145, 22)
#
#Process finished with exit code 0
#
#To check the names of each of the 22 columns in the dataset:
#print(df.columns)
#Returned:
#Index(['Unnamed: 0', 'player_name', 'team_abbreviation', 'age',
#      'player_height', 'player_weight', 'college', 'country', 'draft_year',
#       'draft_round', 'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating',
#       'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season'],
#      dtype='object')
#
#Process finished with exit code 0
#
#To check the type of data in each column of the dataset:
#print(df.dtypes)
#Returned:
#Unnamed: 0             int64
#player_name           object
#team_abbreviation     object
#age                  float64
#player_height        float64
#player_weight        float64
#college               object
#country               object
#draft_year            object
#draft_round           object
#draft_number          object
#gp                     int64
#pts                  float64
#reb                  float64
#ast                  float64
#net_rating           float64
#oreb_pct             float64
#dreb_pct             float64
#usg_pct              float64
#ts_pct               float64
#ast_pct              float64
#season                object
#dtype: object
#
#Process finished with exit code 0
#
#To check for any missing data and if so, the number of missing data in each column:
#
#Returned:
#Unnamed: 0           0
#player_name          0
#team_abbreviation    0
#age                  0
#player_height        0
#player_weight        0
#college              0
#country              0
#draft_year           0
#draft_round          0
#draft_number         0
#gp                   0
#pts                  0
#reb                  0
#ast                  0
#net_rating           0
#oreb_pct             0
#dreb_pct             0
#usg_pct              0
#ts_pct               0
#ast_pct              0
#season               0
#dtype: int64
#
#Process finished with exit code 0
#
#To drop any duplicated values using columns 'player_name' and 'country' and create
# a new dataframe 'df_unique'.  Also, check the revised size:
#df_unique = df.drop_duplicates(subset= ["player_name", "country"])
#print(df_unique.shape)
#print(df_unique)
#Returned:
#(2238, 22)
#
#Process finished with exit code 0
#
#To check Lebron James point averages for each season:
#print(df.loc[df.player_name == 'LeBron James', ['player_name', 'pts', 'season']])
#Returned
#      player_name   pts   season
#3120   LeBron James  20.9  2003-04
#3617   LeBron James  27.2  2004-05
#4075   LeBron James  31.4  2005-06
#4778   LeBron James  27.3  2006-07
#5104   LeBron James  30.0  2007-08
#5430   LeBron James  28.4  2008-09
#6127   LeBron James  29.7  2009-10
#6266   LeBron James  26.7  2010-11
#7004   LeBron James  27.1  2011-12
#7428   LeBron James  26.8  2012-13
#7954   LeBron James  27.1  2013-14
#8322   LeBron James  25.3  2014-15
#8640   LeBron James  25.3  2015-16
#9220   LeBron James  26.4  2016-17
#10028  LeBron James  27.5  2017-18
#10520  LeBron James  27.4  2018-19
#11042  LeBron James  25.6  2019-20
#
#To check Kawhi Leonard point averages for each season:
#print(df.loc[df.player_name == 'Kawhi Leonard', ['player_name', 'pts', 'season']])
#Returned
#         player_name   pts   season
#7016   Kawhi Leonard   7.9  2011-12
#7467   Kawhi Leonard  11.9  2012-13
#8088   Kawhi Leonard  12.8  2013-14
#8329   Kawhi Leonard  16.5  2014-15
#8782   Kawhi Leonard  21.2  2015-16
#9185   Kawhi Leonard  25.5  2016-17
#10064  Kawhi Leonard  16.2  2017-18
#10550  Kawhi Leonard  26.6  2018-19
#11070  Kawhi Leonard  26.9  2019-20
#
#To check Kevin Durant point averages for each season:
#print(df.loc[df.player_name == 'Kevin Durant', ['player_name', 'pts', 'season']])
#Returned
#       player_name   pts   season
#5164   Kevin Durant  20.3  2007-08
#5411   Kevin Durant  25.3  2008-09
#6163   Kevin Durant  30.1  2009-10
#6264   Kevin Durant  27.7  2010-11
#7024   Kevin Durant  28.0  2011-12
#7459   Kevin Durant  28.1  2012-13
#7972   Kevin Durant  32.0  2013-14
#8338   Kevin Durant  25.4  2014-15
#8805   Kevin Durant  28.2  2015-16
#9192   Kevin Durant  25.1  2016-17
#10094  Kevin Durant  26.4  2017-18
#10494  Kevin Durant  26.0  2018-19
#
#Process finished with exit code 0


#To check the average assists per season for John Stockton:
#print(df.loc[df.player_name == 'John Stockton'].ast.mean())
#Returned
#5.722222222222222
#
#SORTING
#To check all the players from Greece
#print(df.query("country == 'Greece'"))
#Returned
#      Unnamed: 0             player_name  ... ast_pct   season
#1840         1840         Jake Tsakalidis  ...   0.033  2000-01
#2525         2525          Antonis Fotsis  ...   0.057  2001-02
#2533         2533         Jake Tsakalidis  ...   0.022  2001-02
#2769         2769         Jake Tsakalidis  ...   0.038  2002-03
#2850         2850      Efthimios Rentzias  ...   0.086  2002-03
#3419         3419         Jake Tsakalidis  ...   0.054  2003-04
#3877         3877         Jake Tsakalidis  ...   0.061  2004-05
#4326         4326         Jake Tsakalidis  ...   0.030  2005-06
#4526         4526         Jake Tsakalidis  ...   0.022  2006-07
#7933         7933   Giannis Antetokounmpo  ...   0.120  2013-14
#8327         8327     Kostas Papanikolaou  ...   0.166  2014-15
#8367         8367   Giannis Antetokounmpo  ...   0.133  2014-15
#8803         8803     Kostas Papanikolaou  ...   0.077  2015-16
#8963         8963  Thanasis Antetokounmpo  ...   0.000  2015-16
#9065         9065   Giannis Antetokounmpo  ...   0.195  2015-16
#9521         9521    Georgios Papagiannis  ...   0.085  2016-17
#9526         9526   Giannis Antetokounmpo  ...   0.269  2016-17
#9594         9594   Giannis Antetokounmpo  ...   0.237  2017-18
#9597         9597    Georgios Papagiannis  ...   0.097  2017-18
#10111       10111   Giannis Antetokounmpo  ...   0.294  2018-19
#10505       10505    Kostas Antetokounmpo  ...   0.000  2018-19
#10638       10638   Giannis Antetokounmpo  ...   0.330  2019-20
#10994       10994  Thanasis Antetokounmpo  ...   0.130  2019-20
#11026       11026    Kostas Antetokounmpo  ...   0.167  2019-20
#[24 rows x 22 columns]
#Process finished with exit code 0
#
#GROUPING
#Group the dataset by player then season in ascending order:
#df_grouped = df.groupby(['player_name', 'season'])
#print(df_grouped.first())
#Returned
#                           Unnamed: 0 team_abbreviation  ...  ts_pct  ast_pct
#player_name        season                                 ...
#A.C. Green         1996-97         138               DAL  ...   0.523    0.045
#                   1997-98         800               DAL  ...   0.496    0.074
#                   1998-99        1054               DAL  ...   0.441    0.043
#                   1999-00        1319               LAL  ...   0.482    0.058
#                   2000-01        1948               MIA  ...   0.492    0.050
#...                                ...               ...  ...     ...      ...
#Zydrunas Ilgauskas 2007-08        5250               CLE  ...   0.522    0.082
#                   2008-09        5696               CLE  ...   0.523    0.060
#                   2009-10        6085               CLE  ...   0.491    0.058
#                   2010-11        6676               MIA  ...   0.531    0.033
#Zylan Cheatham     2019-20       10980               NOP  ...   0.400    0.133
#
#[11141 rows x 20 columns]
##Process finished with exit code 0
#
#Plot Lebron James average points per season:
#lebron_avg_pts = df.loc[df.player_name == 'LeBron James', ['pts','season']]
#plt.plot(lebron_avg_pts["season"], lebron_avg_pts["pts"])
#plt.ylabel('Points Per Game')
#plt.xticks(rotation=90)
#plt.title("Lebron James Average Points Per Season")
#plt.xlabel('Season')
#plt.show()
#Returned - graph saved to LAN folder
#
#Plot comparison between Lebron James v Kawhi Leonard v Kevin Durant average points per season:
#df[df['player_name'] == "LeBron James"] ["pts"] [(df["season"]>= "2011-12")].hist(alpha=0.7)
#df[df['player_name'] == "Kawhi Leonard"] ["pts"] [(df["season"]>= "2011-12")].hist(alpha=0.5)
#df[df['player_name'] == "Kevin Durant"] ["pts"] [(df["season"]>= "2011-12")].hist(alpha=0.4)
#plt.title("Lebron James v Kawhi Leonard v Kevin Durant Average Points Per Season")
#plt.legend(["LBJ", "KL", "KD"])
#plt.ylabel('Points Per Game')
#plt.xlabel('Season')
#plt.xticks(rotation=90)
#plt.show()
#Returned - graph saved to LAN folder
#
#Plot comparison of all teams on average - points, rebounds and assists:
#type = ['pts', 'reb', 'ast']
#all_teams = df.groupby('team_abbreviation')[type].mean()
#print(all_teams)
#
#Plot comparison of all players on average - points, rebounds and assists:
#type = ['pts', 'reb', 'ast']
#all_players = df.groupby('player_name')[type].mean()
#print(all_players)
#
#To sort Players by tallest to smallest:
#print(df.sort_values("player_height", ascending= False))
#
##To group Players by average height - below works.  Need to insert code to show 'tallest to smallest':
#type = ['player_height']
#players = (df.groupby("player_name")[type].mean())
#print(players)
#
#Players who are above the avg height (>=201cm) and below the avg weight (<=101 lbs), sorted by tallest:
height_weight_avg= df[(df['player_height'] >= 201) & (df['player_weight'] <= 101)]
tallest_height_weight_avg = height_weight_avg.sort_values('player_height', ascending= False)
print(tallest_height_weight_avg)

