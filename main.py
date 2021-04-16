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
#To drop any duplicated values using columns 'player_name' and 'college' and create
# a new dataframe 'df_unique'.  Also, check the revised size:
#df_unique = df.drop_duplicates(subset= ["player_name", "college"])
#print(df_unique.shape)
#print(df_unique)
#Returned:
#([2278 rows x 22 columns]
##Process finished with exit code 0
#
#To check the median of the DataFrame:
#print(df.median())
#Returned
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
#To check statistical overview of data:
#print(df.describe())
#Returned
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
#To check each player's median points:
#players_avg_pts = df.groupby(['player_name'])
#print(players_avg_pts['pts'].median())
#Returned
#player_name
#A.C. Green             5.0
#A.J. Bramlett          1.0
#A.J. Guyton            5.4
#AJ Hammons             2.2
#AJ Price               5.8
#                      ...
#Zion Williamson       23.6
#Zoran Dragic           1.8
#Zoran Planinic         3.4
#Zydrunas Ilgauskas    13.9
#Zylan Cheatham         1.3
#Name: pts, Length: 2235, dtype: float64
#Process finished with exit code 0
#
#To check the median points for a specific player:
#players_avg_pts = df.groupby(['player_name'])
#print(players_avg_pts['pts'].median().loc['Seth Curry'])
#Returned
#7.35
#
#
#To check Lebron James point averages for each season:
#lbj_avg_pts = df.loc[df.player_name == 'LeBron James', ['player_name', 'pts', 'season']]
#print(lbj_avg_pts)
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
#kl_avg_pts = df.loc[df.player_name == 'Kawhi Leonard', ['player_name', 'pts', 'season']]
#print(kl_avg_pts)
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
#kd_avg_pts = df.loc[df.player_name == 'Kevin Durant', ['player_name', 'pts', 'season']]
#print(kd_avg_pts)
#
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
#
#SORTING
#To sort by NBA Team and then colleges for the first 10 rows:
#print(df[['team_abbreviation', 'college']].head(10))
#Returned
#  team_abbreviation                      college
#0               CHI  Southeastern Oklahoma State
#1               LAC                      Florida
#2               TOR                Detroit Mercy
#3               DAL                         UCLA
#4               MIA                    Villanova
#5               HOU                     Illinois
#6               LAL                       Temple
#7               LAL                      Clemson
#8               ATL                   Washington
#9               MIL                      Memphis
#Process finished with exit code 0

#To sort on Team and then points in ascending order:
#print(df.sort_values(by=['team_abbreviation', 'pts'], ascending=[True, True]))
#Returned
#Unnamed: 0      player_name team_abbreviation  ...  ts_pct  ast_pct   season
#33             33   Derrick Alston               ATL  ...   0.000    0.000  1996-97
#156           156   Anthony Miller               ATL  ...   0.000    0.000  1996-97
#1862         1862       Ira Bowman               ATL  ...   0.000    0.636  2000-01
#1912         1912       Andy Panko               ATL  ...   0.000    0.000  2000-01
#2600         2600  Dickey Simpkins               ATL  ...   0.000    0.500  2001-02
#...           ...              ...               ...  ...     ...      ...      ...
#3953         3953   Gilbert Arenas               WAS  ...   0.565    0.224  2004-05
#10235       10235     Bradley Beal               WAS  ...   0.581    0.233  2018-19
#4451         4451   Gilbert Arenas               WAS  ...   0.565    0.257  2006-07
#4343         4343   Gilbert Arenas               WAS  ...   0.581    0.261  2005-06
#10766       10766     Bradley Beal               WAS  ...   0.580    0.282  2019-20
#[11145 rows x 22 columns]
#Process finished with exit code 0

#To check all the players from Greece:
#players_greece = df.query("country == 'Greece'")
#print(players_greece)
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
#To check which colleges have the largest number of players:
#college_number_players = df["college"].value_counts()
#print(college_number_players)
#Returned
#None                              1684
#Kentucky                           360
#Duke                               331
#North Carolina                     318
#UCLA                               280
#                                  ...
#Stony Brook, N.Y.                    1
#Augusta State                        1
#Northwestern State                   1
#Indian Hills Community College       1
#Lebanon Valley                       1
#Name: college, Length: 316, dtype: int64
#Process finished with exit code 0
#
#To sort the top 10 teams which have the largest number of players:
#df_teams_number = df["team_abbreviation"].value_counts()
#print((df_teams_number).head(10))
#
#Returned
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
#
#GROUPING and INDEXING
#Group player and then group by season:
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
#Process finished with exit code 0
#
##To group players by selecting a specific team:
#teams_grp = df.groupby(['team_abbreviation'])
#print(teams_grp.get_group('BOS'))
#Returned
#Unnamed: 0       player_name team_abbreviation  ...  ts_pct  ast_pct   season
#20             20     Eric Williams               BOS  ...   0.533    0.087  1996-97
#41             41        Dino Radja               BOS  ...   0.471    0.092  1996-97
#94             94  Frank Brickowski               BOS  ...   0.512    0.116  1996-97
#102           102        Greg Minor               BOS  ...   0.519    0.103  1996-97
#108           108         Dee Brown               BOS
#[367 rows x 22 columns]
#Process finished with exit code 0
#
#To index on team and college by grouping teams by colleges showing how many players from each college
# when to each team:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts())
#Returned
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
#To index on team and college by grouping teams by colleges showing the percentage of players from each college:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts(normalize=True))
#Returned
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
#To index on college by grouping colleges to show the percentage of players for a specific team:
#teams_college_grp = teams_grp = df.groupby(['team_abbreviation'])
#print(teams_college_grp['college'].value_counts(normalize=True).loc['LAL'])
#plt.plot()
#Returned
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
#Plot Lebron James average points per season:
#lebron_avg_pts = df.loc[df.player_name == 'LeBron James', ['season','pts']]
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
#all_teams_pts_reb_ast = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts_reb_ast.sort_values(by=['pts', 'reb', 'ast'], ascending= [False, True, True], inplace= True)
#print(all_teams_pts_reb_ast)
#Returned
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
#Plot comparison for the top 10 teams with average points per player:
#type = ['pts']
#all_teams_pts = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts.sort_values(['pts'], ascending= [False], inplace= True)
#plt.title("Top 10 NBA Teams with avg points per player")
#plt.ylabel('Points Per Game')
#plt.xlabel('Teams')
#plt.xticks(rotation=90)
#plt.plot((all_teams_pts).head(10))
#plt.show()
#Returned - LINE GRAPH SAVED ON LAN folder
#
##Plot comparison for the top 10 teams with average points per player - SEABORN - YOU R HERE!!!:
#type = ['pts']
#all_teams_pts = df.groupby('team_abbreviation')[type].mean()
#all_teams_pts.sort_values(['pts'], ascending= [False], inplace= True)
#plt.title("Top 10 NBA Teams with avg points per player")
#plt.ylabel('Points Per Game')
#plt.xlabel('Teams')
#plt.xticks(rotation=90)
#plt.plot((all_teams_pts).head(10))
#plt.show()
#sns.set(color_codes=True)
#sns.histplot(all_teams_pts ['pts'], color ='r')
#plt.show()
#sns.relplot(x="college", kind= scatter, col= 'reb')
#plt.show()

#Plot comparison of all players on average - points, rebounds and assists:
#type = ['pts', 'reb', 'ast']
#all_players = df.groupby('player_name')[type].mean()
#print(all_players)
#
#Returned
#                         pts       reb       ast
#player_name
#A.C. Green           5.780000  6.060000  0.860000
#A.J. Bramlett        1.000000  2.800000  0.000000
#A.J. Guyton          3.800000  0.700000  1.566667
#AJ Hammons           2.200000  1.600000  0.200000
#AJ Price             5.350000  1.333333  2.000000
#...                       ...       ...       ...
#Zion Williamson     23.600000  6.800000  2.200000
#Zoran Dragic         1.800000  0.500000  0.300000
#Zoran Planinic       3.833333  1.333333  1.100000
#Zydrunas Ilgauskas  12.938462  7.338462  1.092308
#Zylan Cheatham       1.300000  2.000000  0.700000
#[2235 rows x 3 columns]
#Process finished with exit code 0
#
#SORTING and GROUPING
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
#type = ['player_height']
#players_avg_height = (df.groupby("player_name")[type].mean())
#print(players_avg_height)
#
#Returned
#                    player_height
#player_name
#A.C. Green                 205.74
#A.J. Bramlett              208.28
#A.J. Guyton                185.42
#AJ Hammons                 213.36
#AJ Price                   187.96
#...                           ...
#Zion Williamson            198.12
#Zoran Dragic               195.58
#Zoran Planinic             200.66
#Zydrunas Ilgauskas         220.98
#Zylan Cheatham             195.58
#[2235 rows x 1 columns]
#Process finished with exit code 0
#
#Players who are above the avg height (>=201cm) and below the avg weight (<=101 lbs), sorted by tallest:
#height_weight_avg= df[(df['player_height'] >= 201) & (df['player_weight'] <= 101)]
#tallest_height_weight_avg = height_weight_avg.sort_values('player_height', ascending= False)
#print(tallest_height_weight_avg)
#
#Returned
#      Unnamed: 0      player_name team_abbreviation  ...  ts_pct  ast_pct   season
#1280        1280      Keith Closs               LAC  ...   0.584    0.000  1998-99
#520          520      Keith Closs               LAC  ...   0.482    0.041  1997-98
#1690        1690      Keith Closs               LAC  ...   0.514    0.048  1999-00
#880          880     Bruno Sundov               DAL  ...   0.286    0.143  1998-99
#1514        1514     Bruno Sundov               DAL  ...   0.408    0.051  1999-00
#...          ...              ...               ...  ...     ...      ...      ...
#7271        7271  Reggie Williams               CHA  ...   0.517    0.180  2012-13
#6051        6051  Reggie Williams               GSW  ...   0.588    0.125  2009-10
#6857        6857  Reggie Williams               CHA  ...   0.503    0.154  2011-12
#8457        8457  Reggie Williams               SAS  ...   0.454    0.169  2014-15
#7647        7647  Reggie Williams               OKC  ...   0.611    0.143  2013-14
#[925 rows x 22 columns]
#Process finished with exit code 0
#