# Tweet_Cleaner

*(This program is designed specifically for users that are not familiarized with programming languages and want to extract tweets using Tweepy)*

### Uses

-Reads a raw text obtained with the Tweepy application *(including special characters as emojis)*


-Extracts complete tweets without metadata *(date, time, etc.)*


-Filters clean tweets:

--By length *(equal or more than 50 characters)*
	
--Excludes URLs, hashtags, @profile names, offensive words and abbreviations


-Writes Tweets in an output file *(it does not delete emojis)*


### How to use it

-Change the name of Input and Output files
**IMPORTANT! Write the entire path where these are files located!**
	
	e.g. /Home/User1/Desktop/input.txt

-Open a terminal and execute this code:
	
	python3 Tweepy_clean_files.py


### Change filter settings

**-Lenght:** Simply change number 50 with another value

**-Filter settings:** *"forbiden_characters"* is a list of characters that the user doesn't want to find in the output file. All tweets that contain any of these words or characters will be removed.

-ADD more filter settings: Write new words in the list as described below: 

		e.g. forbiden_characters = ( "word1", "newword" )

-REMOVE filter settings: Recommendation, **do not remove "..."** from the list because it removes tweets that are incomplete or bugged. 


