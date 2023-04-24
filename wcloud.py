from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk


def read_file(filename):
	with open(filename, "r") as f:
                return f.read()


def split_alpha_words(token_list):
	alpha_tokens = list()
	for token in token_list:
		if token.isalpha():
			alpha_tokens.append(token)
	return alpha_tokens


def normalize_words(words_list):
	normalized_list = list()
	for word in words_list:
		normalized_list.append(word.lower())
	return normalized_list


def get_words_from_list(words_list):
	return ' '.join([word for word in words_list])


def build_word_cloud(words):
	return WordCloud(width= 800, height= 500, 
		max_font_size = 110, 
		collocations = False
	).generate(words)


def plot_image(word_cloud):
	plt.figure(figsize=(15,9))
	plt.imshow(word_cloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()


filename = input("Digite o nome do arquivo contendo textos? ")

file_text = read_file(filename)

tokenizer_words = nltk.tokenize.word_tokenize(file_text)

words_list = normalize_words(split_alpha_words(tokenizer_words))

words_counter = len(set(words_list))

print(f"Document has {words_counter} different words")
print("Building a WordCloud...")

plot_image(build_word_cloud(get_words_from_list(words_list)))
