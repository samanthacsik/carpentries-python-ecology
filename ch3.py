# Following exercises in Ch 3: Starting with Data

# load libraries [in R: library(pandas)]
import pandas as pd

# load data [in R: readr::surveys_df <- read_csv("data/surveys.csv")]
surveys_df = pd.read_csv("data/surveys.csv")

# print the DataFrame
surveys_df

# head [in R: head(surveys_df)]
surveys_df.head()

### --------------- Exploring Our Species Survey Data --------------- ###

# see type of think surveys_df is [in R: class(surveys_df)]
type(surveys_df)

# what kind of things does surveys_df contain? [in R: str(surveys_df)]
surveys_df.dtypes
# int64: integer (can't have fractional values)
# fload64 (can have fractional values)
# object (in this case, represents strings, such as 'M' and 'F' in the 'sex' column)

# see the size of an object
surveys_df.shape

# column names
surveys_df.columns

# NOTE: methods are like functions, butthey only work on particular kinds of objects (e.g. head() method works on DataFrames)
# you can supply extra info in the parentheses to control behavior

####################################
###### Challenge - DataFrames ######
####################################
surveys_df.columns
surveys_df.shape # returns output as a tuple in (rows, columns) format
surveys_df.head() # prints 5 rows
surveys_df.head(15) # prints 15 rows
surveys_df.tail() # prints last 5 rows

### --------------- Calculating Statistics from Data in a Pandas DataFrame --------------- ###

# begin by exploring data ----
surveys_df.columns

# get a list of all species [in R: unique(surveys_df$species_id)]
species_id_names = pd.unique(surveys_df['species_id'])
species_id_names

####################################
###### Challenge - Statistics ######
####################################

# create list of unique site IDs found in the surveys data
site_names = pd.unique(surveys_df['plot_id'])
len(site_names) # 24 unique site names, vs.
len(species_id_names) # 49 unique species id names

# what is the difference between?
len(site_names) # vs. 
surveys_df['plot_id'].nunique() # helps avoid creating intermediate variables, like 'site_names' but ultimately, both return the same output

### --------------- Groups in Pandas --------------- ###

# calculate basic stats for all records in a single column [in R: summary(surveys_df) -- shows stats for all columns at the same time]
surveys_df['weight'].describe()

# extract specific metric
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()

# group data by sex [in R: grouped_data <- surveys_df %>% group_by(sex) %>% summarize(...)]
grouped_data = surveys_df.groupby('sex')
grouped_data.describe() # sum stats fro all numeric cols by sex
grouped_data.mean(numeric_only=True) # mean for each numeric col by sex

####################################
##### Challenge - Summary Data #####
####################################

# how many recorded indivs are F and how many are M
grouped_data.describe() # 15690 F & 17348 M; some records may have been excluded from the grouping if NAs were present in the 'sex' column

# what happens when you group by 2 cols using the following syntaz and calculate mean values?
grouped_data2 = surveys_df.groupby(['plot_id', 'sex'])
grouped_data2['weight'].mean() # returns mean value for each combo of plot and sex
grouped_data2.mean(numeric_only=True) # same
# mean is not meaningful for some vars (e.g. day, month, year); use 'agg()' to obtain the last survey eyear, median foot-length and mean weight for each plot/sex combo
surveys_df.groupby(['plot_id', 'sex']).agg({"year": 'max', "hindfoot_length": 'median', "weight": 'mean'}) 

# summarize weight vals for each site
surveys_df.groupby(['plot_id'])['weight'].describe()

### --------------- Quickly Creating Summary Counts in Pandas --------------- ###

# count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)

# OR count just the rows that have the species "DO" -- QUESTION: WHAT IS 'DO'?
surveys_df.groupby('species_id')['record_id'].count()['DO']

####################################
##### Challenge - Make A List ######
####################################

# what's another way to create a list of spp and associated 'count' of the records in the data?
surveys_df.groupby('species_id').count()['record_id']

### --------------- Basic Math Functions --------------- ###

# mutiply all weight values by 2 -- QUESTION: UNUSRE THAT THIS WORKED?
surveys_df['weight']*2

