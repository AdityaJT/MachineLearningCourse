from bs4 import BeautifulSoup

soup = BeautifulSoup(open("adityaTaujale.html"))
TextSection = soup.findAll('div','article-text')

AllText = ""
#eliminating html tags
for txt in TextSection:
	AllText += txt.get_text()
	
print("\n")
index = 0
sentences = ""

#while loop to start next new line if "." is found
while index < len(AllText):
	symbol = AllText[index]
	sentences += symbol
	if (symbol == '.' or symbol== '\t'):
		sentences += "\n"
	index += 1
	
#printing the final text	
print(sentences)
