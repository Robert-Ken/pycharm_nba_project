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
##Process finished with exit code 0
#
#To check the median for each column:
#print(df.median())
#Returned:
#Unnamed: 0       5572.00000
#age                27.00000
#player_height     200.66000
#player_weight      99.79024
#gp                 58.00000
#pts                 6.60000
#reb                 3.00000
#ast                 1.20000
#net_rating         -1.30000
#oreb_pct            0.04300
#dreb_pct            0.13200
#usg_pct             0.18200
#ts_pct              0.52100
#ast_pct             0.10200
#dtype: float64
#Process finished with exit code 0
#
#To drop any duplicated values using columns 'player_name' and 'college' and create
# a new dataframe 'df_drop_dup'.  Also, check the revised size:
#df_drop_dup = df.drop_duplicates(subset= ["player_name", "college"])
#print(df_drop_dup.shape)
#Returned:
#([2278 rows x 22 columns]
#Process finished with exit code 0
#
#To show new dataframe removing duplicates on  Player's name, sort in ascending order:
#df_drop_dup = df.drop_duplicates(subset= ["player_name", "college"])
#players_ascending = df_drop_dup.sort_values(by=["player_name"], ascending =[True])
#print(players_ascending.head(10))
#Returned:
#Unnamed: 0     player_name team_abbreviation  ...  ts_pct  ast_pct   season
#138           138      A.C. Green               DAL  ...   0.523    0.045  1996-97
#1538         1538   A.J. Bramlett               CLE  ...   0.190    0.000  1999-00
#1759         1759     A.J. Guyton               CHI  ...   0.495    0.198  2000-01
#9147         9147      AJ Hammons               DAL  ...   0.472    0.038  2016-17
#5805         5805        AJ Price               IND  ...   0.530    0.198  2009-10
#5025         5025    Aaron Brooks               HOU  ...   0.535    0.249  2007-08
#8200         8200    Aaron Gordon               ORL  ...   0.517    0.064  2014-15
#5026         5026      Aaron Gray               CHI  ...   0.529    0.113  2007-08
#8924         8924  Aaron Harrison               CHA  ...   0.371    0.033  2015-16
#10627       10627   Aaron Holiday               IND  ...   0.518    0.180  2018-19
#[10 rows x 22 columns]
#Process finished with exit code 0
#
#Using the new dataframe removing duplicates on  Player's name, sort in ascending order,
#selecting columns 'player_name', 'team_abbreviation', 'college', 'pts':
#df_drop_dup = df.drop_duplicates(subset= ["player_name", "college"])
#players_ascending = df_drop_dup.sort_values(by=["player_name"], ascending =[True])
#players_all_selected = players_ascending[['player_name', 'team_abbreviation', 'college', 'pts']]
#print(players_all_selected.head(10))
#Returned:
#         player_name team_abbreviation       college  pts
#138        A.C. Green               DAL  Oregon State  7.2
#1538    A.J. Bramlett               CLE       Arizona  1.0
#1759      A.J. Guyton               CHI       Indiana  6.0
#9147       AJ Hammons               DAL        Purdue  2.2
#5805         AJ Price               IND   Connecticut  7.3
#5025     Aaron Brooks               HOU        Oregon  5.2
#8200     Aaron Gordon               ORL       Arizona  5.2
#5026       Aaron Gray               CHI    Pittsburgh  4.3
#8924   Aaron Harrison               CHA      Kentucky  0.9
#10627   Aaron Holiday               IND          UCLA  5.9
#Process finished with exit code 0
#
#To sort players based on points (pts) in decending order:
#group_player_avg_pts= df.groupby('player_name').agg({'pts': 'mean', 'reb' : 'mean', 'ast': 'mean'})
#players_ascending_pts = group_player_avg_pts.sort_values(by=['pts'], ascending =[False])
#print(players_ascending_pts.head(10))
#Returned:
#                    pts        reb       ast
#player_name
#LeBron James    27.064706   7.447059  7.441176
#Kevin Durant    26.883333   7.075000  4.125000
#Allen Iverson   26.064286   3.692857  6.000000
#Michael Jordan  25.300000   5.875000  4.200000
#James Harden    25.154545   5.300000  6.263636
#Luka Doncic     24.800000   8.600000  7.350000
#Damian Lillard  24.312500   4.187500  6.537500
#Trae Young      24.250000   4.000000  8.650000
#Kobe Bryant     24.200000   5.200000  4.760000
#Anthony Davis   23.950000  10.387500  2.275000
#Process finished with exit code 0
#
#Plot Players overall average points (pts) for all seasons:
#player_avg_pts= df.groupby('player_name').agg({'pts': 'mean'})
#players_ascending_pts = player_avg_pts.sort_values(by=['pts'], ascending =[False])
#players_pts_plot= players_ascending_pts.head(10)
#players_pts_plot.plot(kind='bar')
#plt.plot(players_pts_plot)
#plt.ylabel('Avg Points')
#plt.xticks(rotation=45)
#plt.title("Top 10 Players average points")
#plt.xlabel('Players')
#plt.show()
#Returned - Bar Chart  saved on LAN folder
#
#To sort players based on rebounds (reb) in decending order:
#group_player_avg_pts= df.groupby('player_name').agg({'pts': 'mean', 'reb' : 'mean', 'ast': 'mean'})
#players_ascending_reb = group_player_avg_pts.sort_values(by=['reb'], ascending =[False])
#print(players_ascending_reb.head(10))
#Returned:
#                          pts        reb       ast
#player_name
#Dennis Rodman        3.825000  14.150000  2.125000
#Andre Drummond      14.350000  13.725000  1.325000
#Jayson Williams     11.466667  13.033333  1.100000
#Dwight Howard       16.500000  12.087500  1.356250
#Charles Barkley     16.250000  12.000000  3.925000
#Karl-Anthony Towns  23.120000  11.660000  2.980000
#Kevin Love          18.283333  11.300000  2.333333
#Deandre Ayton       17.650000  11.150000  1.850000
#Joel Embiid         23.475000  11.050000  3.025000
#DeMarcus Cousins    21.277778  10.833333  3.355556
#Process finished with exit code 0
#
#Plot Players overall average rebounds (reb) for all seasons:
#player_avg_reb= df.groupby('player_name').agg({'reb': 'mean'})
#players_ascending_reb = player_avg_reb.sort_values(by=['reb'], ascending =[False])
#players_reb_plot= players_ascending_reb.head(10)
#players_reb_plot.plot(kind='bar')
#plt.plot(players_reb_plot)
#plt.ylabel('Avg Rebounds')
#plt.xticks(rotation=45)
#plt.title("Top 10 Players average rebounds")
#plt.xlabel('Players')
#plt.show()
#Returned - Bar Chart  saved on LAN folder
#
#To sort players based on assists (ast) in decending order:
#group_player_avg_pts= df.groupby('player_name').agg({'pts': 'mean', 'reb' : 'mean', 'ast': 'mean'})
#players_ascending_ast = group_player_avg_pts.sort_values(by=['ast'], ascending =[False])
#print(players_ascending_ast.head(10))
#
#Returned:
#                         pts       reb       ast
#player_name
#Chris Paul         18.406667  4.506667  9.440000
#John Wall          19.022222  4.244444  9.100000
#Jason Kidd         12.376471  6.241176  8.682353
#Trae Young         24.250000  4.000000  8.650000
#John Stockton      12.185714  2.771429  8.528571
#Rajon Rondo        10.278571  4.764286  8.442857
#Russell Westbrook  23.408333  7.083333  8.225000
#Steve Nash         13.522222  2.911111  8.161111
#Ben Simmons        16.466667  8.233333  8.033333
#Deron Williams     16.358333  3.100000  8.025000
#Process finished with exit code 0
#
#Plot Players overall average assists (ast) for all seasons:
#player_avg_ast= df.groupby('player_name').agg({'ast': 'mean'})
#players_ascending_ast = player_avg_ast.sort_values(by=['ast'], ascending =[False])
#players_ast_plot= players_ascending_ast.head(10)
#players_ast_plot.plot(kind='bar')
#plt.plot(players_ast_plot)
#plt.ylabel('Avg Assists')
#plt.xticks(rotation=45)
#plt.title("Top 10 Players average assists")
#plt.xlabel('Players')
#plt.show()
#Returned - Bar Chart saved on LAN folder
#
#To check statistical overview of data:
#print(df.describe())
#Returned:
#        Unnamed: 0           age  ...        ts_pct       ast_pct
#count  11145.000000  11145.000000  ...  11145.000000  11145.000000
#mean    5572.000000     27.168686  ...      0.508099      0.131078
#std     3217.428709      4.344164  ...      0.098879      0.095017
#min        0.000000     18.000000  ...      0.000000      0.000000
#25%     2786.000000     24.000000  ...      0.478000      0.065000
#50%     5572.000000     27.000000  ...      0.521000      0.102000
#75%     8358.000000     30.000000  ...      0.557000      0.178000
#max    11144.000000     44.000000  ...      1.500000      1.000000
#
#[8 rows x 14 columns]
#Process finished with exit code 0
#
#To check the median points for a specific player:
#players_avg_pts = df.groupby(['player_name'])
#print(players_avg_pts['pts'].median().loc['Seth Curry'])
#Returned:
#7.35
#
#To check Lebron James point averages for each season:
#lbj_avg_pts = df.loc[df.player_name == 'LeBron James', ['player_name', 'pts', 'season']]
#print(lbj_avg_pts)
#Returned:
#       player_name   pts   season
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
#To plot LeBron James average points per season:
#lebron_avg_pts = df.loc[df.player_name == 'LeBron James', ['season','pts']]
#plt.plot(lebron_avg_pts["season"], lebron_avg_pts["pts"])
#plt.ylabel('Points Per Game')
#plt.xticks(rotation=45)
#plt.title("Lebron James Average Points Per Season")
#plt.xlabel('Season')
#plt.show()
#Returned - Graph saved on LAN folder
#
#To check Kawhi Leonard point averages for each season:
#kl_avg_pts = df.loc[df.player_name == 'Kawhi Leonard', ['player_name', 'pts', 'season']]
#print(kl_avg_pts)
#Returned:
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
#kd_avg_pts = df.loc[df.player_name == 'Kevin Durant', ['player_name', 'pts', 'season']]
#print(kd_avg_pts)
#Returned:
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
#Process finished with exit code 0
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
#Percentage of players broken down by country:
#country= (df['country'].value_counts(normalize= True)*100)
#print(country)
#Returned:
#USA                    84.432481
#France                  1.372813
#Canada                  1.256169
#Spain                   0.708838
#Brazil                  0.699865
#                         ...
#Sudan                   0.008973
#Sudan (UK)              0.008973
#Guinea                  0.008973
#Trinidad and Tobago     0.008973
#Ghana                   0.008973
#Name: country, Length: 76, dtype: float64
#Process finished with exit code 0
#
#Create a dictionary using the 'for loop' of the Top 10 countries for percentage of players:
#country= {'USA' : 84.4, 'France' : 1.4, 'Canada' : 1.3, 'Spain' : 0.7, 'Brazil' : 0.7,
#                   'Australia' : 0.6, 'Slovenia' : 0.6, 'Turkey': 0.6, 'Croatia' : 0.6, 'Argentina' : 0.5}
#print(country)
#for country, percentage in country.items():
#    print('Players from' + ' '+ country + ' ' 'account for' + ' ' + str(percentage) + ' ' + '% of NBA players')
#Returned:
#{'USA': 84.4, 'France': 1.4, 'Canada': 1.3, 'Spain': 0.7, 'Brazil': 0.7, 'Australia': 0.6, 'Slovenia': 0.6,
#       'Turkey': 0.6, 'Croatia': 0.6, 'Argentina': 0.5}
#Players from USA account for 84.4 % of NBA players
#Players from France account for 1.4 % of NBA players
#Players from Canada account for 1.3 % of NBA players
#Players from Spain account for 0.7 % of NBA players
#Players from Brazil account for 0.7 % of NBA players
#Players from Australia account for 0.6 % of NBA players
#Players from Slovenia account for 0.6 % of NBA players
#Players from Turkey account for 0.6 % of NBA players
#Players from Croatia account for 0.6 % of NBA players
#Players from Argentina account for 0.5 % of NBA players
#Process finished with exit code 0
#
#Excluding the USA Players, the percentage of Non-USA Players broken down by country:
#players_not_usa = df.query("country != 'USA'")
#print(players_not_usa['country'].value_counts(normalize=True)*100)
#Returned:
#France                 8.818444
#Canada                 8.069164
#Spain                  4.553314
#Brazil                 4.495677
#Australia              4.265130
#                         ...
#Ghana                  0.057637
#Trinidad and Tobago    0.057637
#Sudan (UK)             0.057637
#Angola                 0.057637
#Sudan                  0.057637
#Name: country, Length: 75, dtype: float64
#Process finished with exit code 0
#
#To list the players from France:
#players_france = df.query("country == 'France'")
#print(players_france)
#Returned:
#Unnamed: 0              player_name  ... ast_pct   season
#603           603        Tariq Abdul-Wahad  ...   0.087  1997-98
#1041         1041        Tariq Abdul-Wahad  ...   0.062  1998-99
#1623         1623        Tariq Abdul-Wahad  ...   0.098  1999-00
#2058         2058             Jerome Moiso  ...   0.043  2000-01
#2103         2103        Tariq Abdul-Wahad  ...   0.087  2000-01
#...           ...                      ...  ...     ...      ...
#10891       10891              Rudy Gobert  ...   0.066  2019-20
#10961       10961          Vincent Poirier  ...   0.084  2019-20
#10969       10969           William Howard  ...   0.200  2019-20
#11000       11000  Timothe Luwawu-Cabarrot  ...   0.052  2019-20
#11103       11103            Nicolas Batum  ...   0.173  2019-20
#[153 rows x 22 columns]
#Process finished with exit code 0
#
#To list the colleges with the largest number of players, in percentage terms:
#college_number_players = (df["college"].value_counts(normalize=True)*100)
#print(college_number_players)
#Returned:
#None                   15.109915
#Kentucky                3.230148
#Duke                    2.969942
#North Carolina          2.853297
#UCLA                    2.512337
#                         ...
#Wisconsin-Green Bay     0.008973
#Montevallo              0.008973
#Walsh                   0.008973
#North Texas             0.008973
#Tennessee Tech          0.008973
#Name: college, Length: 316, dtype: float64
#Process finished with exit code 0
#
#Create a dictionary using the 'for loop' of the Top 10 colleges for percentage of players:
#college= {'No College' : 15.1, 'Kentucky' : 3.2, 'Duke' : 2.9, 'North Carolina' : 2.9, 'UCLA ' : 2.5,
#                   'Arizona' : 2.3, 'Kansas' : 2.3, 'Connecticut ': 1.9, 'Georgia Tech' : 1.6, 'Florida ' : 1.6}
#print(college)
#for college, percentage in college.items():
#    print('Players who attended' + ' '+ college + ' ' 'account for' + ' ' + str(percentage) + ' ' + '% of NBA players')
#Returned:
#{'No College': 15.1, 'Kentucky': 3.2, 'Duke': 2.9, 'North Carolina': 2.9, 'UCLA ': 2.5, 'Arizona': 2.3, 'Kansas': 2.3,
#       'Connecticut ': 1.9, 'Georgia Tech': 1.6, 'Florida ': 1.6}
#Players who attended No College account for 15.1 % of NBA players
#Players who attended Kentucky account for 3.2 % of NBA players
#Players who attended Duke account for 2.9 % of NBA players
#Players who attended North Carolina account for 2.9 % of NBA players
#Players who attended UCLA  account for 2.5 % of NBA players
#Players who attended Arizona account for 2.3 % of NBA players
#Players who attended Kansas account for 2.3 % of NBA players
#Players who attended Connecticut  account for 1.9 % of NBA players
#Players who attended Georgia Tech account for 1.6 % of NBA players
#Players who attended Florida  account for 1.6 % of NBA players
#Process finished with exit code 0
#
##Plot the Top 10 colleges with players in the NBA:
#college_number_players = (df["college"].value_counts(normalize=True)*100)
#plt.plot(college_number_players.head(10))
#plt.ylabel('% players')
#plt.xticks(rotation=45)
#plt.title("Top 10 Colleges with Players in the NBA")
#plt.xlabel('Colleges')
#plt.show()
#Returned: Graph saved on LAN folder
#
#To list the top 10 teams which have the largest number of players:
#df_teams_number = df["team_abbreviation"].value_counts()
#print((df_teams_number).head(10))
#Returned:
#CLE    390
#TOR    390
#LAC    389
#MIA    387
#DAL    384
#ATL    383
#PHI    380
#WAS    379
#HOU    378
#SAS    377
#Name: team_abbreviation, dtype: int64
#Process finished with exit code 0
#
#Plot the Top 10 teams with most players in the NBA:
#df_teams_number = df["team_abbreviation"].value_counts()
#plt.plot(df_teams_number.head(10))
#plt.ylabel('No. of players')
#plt.xticks(rotation=45)
#plt.title("Top 10 Teams with Players in the NBA")
#plt.xlabel('Teams')
#plt.show()
#Returned: Graph saved on LAN folder
#
#Group by player and then group by season:
#df_grouped = df.groupby(['player_name', 'season'])
#print(df_grouped.first())
#Returned:
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
#Process finished with exit code 0
#
##To group players by selecting a specific team:
#teams_grp = df.groupby(['team_abbreviation'])
#print(teams_grp.get_group('BOS'))
#
#Returned:
#Unnamed: 0       player_name team_abbreviation  ...  ts_pct  ast_pct   season
#20             20     Eric Williams               BOS  ...   0.533    0.087  1996-97
#41             41        Dino Radja               BOS  ...   0.471    0.092  1996-97
#94             94  Frank Brickowski               BOS  ...   0.512    0.116  1996-97
#102           102        Greg Minor               BOS  ...   0.519    0.103  1996-97
#108           108         Dee Brown               BOS  ...   0.455    0.202  1996-97
#...           ...               ...               ...  ...     ...      ...      ...
#10950       10950        Tacko Fall               BOS  ...   0.713    0.000  2019-20
#10961       10961   Vincent Poirier               BOS  ...   0.540    0.084  2019-20
#11007       11007    Tremont Waters               BOS  ...   0.438    0.185  2019-20
#11076       11076      Kemba Walker               BOS  ...   0.574    0.236  2019-20
#11124       11124      Marcus Smart               BOS  ...   0.519    0.215  2019-20
#[367 rows x 22 columns]
#Process finished with exit code 0
#
#To group by teams and colleges showing how many players from each college
# when to each team:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts())
#Returned:
#team_abbreviation  college
#ATL                None              60
#                   Georgia Tech      14
#                   Duke              13
#                   Arizona           11
#                   North Carolina    11
#                                     ..
#WAS                Utah               1
#                   Virginia Tech      1
#                   Washington         1
#                   Wichita State      1
#                   Wisconsin          1
#Name: college, Length: 2946, dtype: int64
#Process finished with exit code 0
#
#To group teams by colleges showing the percentage of players from each college:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts(normalize=True))
#Returned:
#team_abbreviation  college
#ATL                None              0.156658
#                   Georgia Tech      0.036554
#                   Duke              0.033943
#                   Arizona           0.028721
#                   North Carolina    0.028721
#                                       ...
#WAS                Utah              0.002639
#                   Virginia Tech     0.002639
#                   Washington        0.002639
#                   Wichita State     0.002639
#                   Wisconsin         0.002639
#Name: college, Length: 2946, dtype: float64
#Process finished with exit code 0
#
#To group colleges to show the percentage of players for a specific team:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts(normalize=True).loc['LAL'])
#Returned:
#college
#None                    0.191375
#Arizona                 0.045822
#North Carolina          0.040431
#UCLA                    0.040431
#Arkansas-Little Rock    0.032345
#                          ...
#Tulsa                   0.002695
#University of Dayton    0.002695
#Utah Valley             0.002695
#Washington              0.002695
#Xavier                  0.002695
#Name: college, Length: 86, dtype: float64
#Process finished with exit code 0
#
#To filter players for a specific team, e.g. LA Lakers (LAL) and show how many players per college:
#filt = df['team_abbreviation'] == 'LAL'
#print(df.loc[filt] ['college'].value_counts())
#Returned:
#None                           71
#Arizona                        17
#North Carolina                 15
#UCLA                           15
#Duke                           12
#Name: college, Length: 86, dtype: int64
#Process finished with exit code 0
#
#
#Plot comparison of all teams on average - points, rebounds and assists:
#type = ['pts', 'reb', 'ast']
#all_teams_pts_reb_ast = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts_reb_ast.sort_values(by=['pts', 'reb', 'ast'], ascending= [False, True, True], inplace= True)
#print(all_teams_pts_reb_ast)
#Returned:
#                        pts       reb       ast
# team_abbreviation
# NOP                8.972951  3.758197  2.050820
# GSW                8.592021  3.770479  1.978989
# SAC                8.562291  3.690503  1.809218
# LAL                8.535849  3.771968  1.942318
# PHX                8.508011  3.583149  1.915470
# HOU                8.383069  3.684127  1.751587
# DEN                8.382527  3.681720  1.884946
# MIN                8.329508  3.604372  1.942623
# MIL                8.322911  3.618329  1.907817
# NOK                8.290625  3.718750  1.493750
# NYK                8.242318  3.671968  1.733423
# WAS                8.234565  3.563061  1.809499
# LAC                8.215424  3.511568  1.786632
# BOS                8.206540  3.519346  1.848501
# IND                8.181671  3.598922  1.805391
# DAL                8.126042  3.515104  1.761198
# BKN                8.122857  3.392857  1.755000
# MIA                8.120155  3.573902  1.749096
# OKC                8.113333  3.510769  1.630769
# CHI                8.098916  3.632520  1.903523
# ORL                7.995652  3.496467  1.758152
# PHI                7.947632  3.588684  1.742105
# DET                7.944972  3.439385  1.774581
# POR                7.930245  3.524796  1.725886
# CHA                7.900394  3.522441  1.750000
# UTA                7.898889  3.444167  1.853611
# MEM                7.898095  3.388571  1.747937
# CHH                7.883146  3.512360  1.865169
# CLE                7.878205  3.565128  1.737692
# NOH                7.853147  3.511189  1.759441
# SAS                7.824934  3.406897  1.763660
# NJN                7.796498  3.540856  1.719455
# SEA                7.789560  3.341758  1.719780
# TOR                7.778974  3.443077  1.699231
# ATL                7.703655  3.461619  1.688251
# VAN                7.540278  3.443056  1.881944
# Process finished with exit code 0
#
#
#Plot comparison for the average points per player for Top 10 Teams:
#type = ['pts']
#all_teams_pts = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts.sort_values(['pts'], ascending= [False], inplace= True)
#plt.title("Avg points per player for the Top 10 Teams")
#plt.ylabel('Points Per Game')
#plt.xlabel('Teams')
#plt.xticks(rotation=90)
#plt.plot((all_teams_pts).head(10))
#plt.show()
#Returned - LINE GRAPH SAVED ON LAN folder
#
##Plot comparison for the top 10 teams with average points per player:
#type = ['pts']
#all_teams_pts = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts.sort_values(['pts'], ascending= [False], inplace= True)
#plt.title("Top 10 NBA Teams with avg points per player")
#plt.ylabel('Points Per Game')
#plt.xlabel('Teams')
#plt.xticks(rotation=90)
#plt.plot((all_teams_pts).head(10))
#plt.show()
#Returned: Graph saved to LAN folder
#
#To sort Players by tallest to smallest:
#print(df.sort_values("player_height", ascending= False))
#
#Returned
#Unnamed: 0       player_name team_abbreviation  ...  ts_pct  ast_pct   season
#1212        1212  Gheorghe Muresan               NJN  ...   0.000    0.000  1998-99
#1408        1408  Gheorghe Muresan               NJN  ...   0.492    0.056  1999-00
#92            92  Gheorghe Muresan               WAS  ...   0.618    0.024  1996-97
#3266        3266     Shawn Bradley               DAL  ...   0.523    0.038  2003-04
#3662        3662          Yao Ming               HOU  ...   0.614    0.048  2004-05
#...          ...               ...               ...  ...     ...      ...      ...
#1123        1123     Muggsy Bogues               GSW  ...   0.539    0.338  1998-99
#401          401     Muggsy Bogues               CHH  ...   0.554    0.366  1996-97
#483          483     Muggsy Bogues               GSW  ...   0.492    0.344  1997-98
#2020        2020     Muggsy Bogues               TOR  ...   0.000    0.294  2000-01
#1705        1705     Muggsy Bogues               TOR  ...   0.517    0.266  1999-00
##[11145 rows x 22 columns]
#Process finished with exit code 0
#
##To group Players by average height - below works.  Need to insert code to show 'tallest to smallest':
#group_player_avg_height= df.groupby('player_name').agg({'player_height': 'mean'})
#players_ascending_height = group_player_avg_height.sort_values(by=['player_height'], ascending =[False])
#print(players_ascending_height)
#                player_height
#player_name
#Gheorghe Muresan       231.1400
#Shawn Bradley          228.6000
#Yao Ming               228.2825
#Pavel Podkolzin        226.0600
#Sim Bhullar            226.0600
#...                         ...
#Chris Clemons          175.2600
#Nate Robinson          175.2600
#Spud Webb              167.6400
#Earl Boykins           165.1000
#Muggsy Bogues          160.0200
#[2235 rows x 1 columns]
#Process finished with exit code 0
#
#Plot the tallest players in the NBA:
#group_player_avg_height= df.groupby('player_name').agg({'player_height': 'mean'})
#players_ascending_height = group_player_avg_height.sort_values(by=['player_height'], ascending =[False])
#plt.plot((players_ascending_height).head(10))
#plt.xticks(rotation=90)
#plt.title("Top 10 tallest players in the NBA")
#plt.ylabel('Height (cm)')
#plt.xlabel('Players')
#plt.show()
#Returned: Graph saved to LAN folder
#
#Players who are above the avg height (>=201cm) and below the avg weight (<=101 lbs), sorted by tallest:
#group_height_weight= df.groupby('player_name').agg({'player_height': 'mean', 'player_weight' : 'mean'})
#players_ascending_height_weight = group_height_weight.sort_values(by=['player_height', 'player_weight'],
#                                                                  ascending =[False, True])
#print((players_ascending_height_weight).head(10))
#Returned:
#                  player_height  player_weight
#player_name
#Gheorghe Muresan        231.1400     137.438376
#Shawn Bradley           228.6000     119.798687
#Yao Ming                228.2825     139.819734
#Pavel Podkolzin         226.0600     117.933920
#Slavko Vranes           226.0600     124.737800
#Tacko Fall              226.0600     141.067112
#Sim Bhullar             226.0600     163.293120
#Rik Smits               223.5200     120.201880
#Priest Lauderdale       223.5200     151.499728
#Boban Marjanovic        221.4880     131.541680
#Process finished with exit code 0
#
