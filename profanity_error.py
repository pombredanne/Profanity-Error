import urllib

def read_text():
	quotes = open ("/home/caramethylate/Desktop/Dev/Python/Profanity Error/movie_quotes.txt") #built in fuction ; returns object of the file type
	contents_of_file = quotes.read()
	print contents_of_file
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print "Curse Words detected"
	else:
		print "No Curse Words"

	

read_text()
