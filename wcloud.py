#!/usr/bin/env python3
# coding: utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import PyPDF2
import os
import numpy as np
import pandas as pd
from PIL import Image
import sys


# GLOBAL VARIABLES
text_file = ""
file_extension = ""
mask_file = ""
dictionary = "english"
background = "black"
width = 15
height = 9
pixel_width = 800
pixel_height = 500
max_font = 110


def read_file(filename):
	with open(filename, "r") as f:
                return f.read()


def read_text_from_pdf(pdf_file):
    pdf = open(pdf_file, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    num_pages = len(reader.pages)
    text_extracted = ""
    for n in range(0,num_pages):
        text_extracted += reader.pages[n].extract_text()
    pdf.close()
    return text_extracted


def get_alpha_tokens(token_list):
	alpha_tokens = list()
	for token in token_list:
		if token.isalpha():
			alpha_tokens.append(token)
	return alpha_tokens


def normalize_words_list(words_list):
	normalized_list = list()
	for word in words_list:
		normalized_list.append(word.lower())
	return normalized_list


def build_words_list(text):
	return normalize_words_list(
                        get_alpha_tokens(
                                nltk.tokenize.word_tokenize(text)
                        )
                )


def get_words_from_list(words_list):
	return ' '.join([word for word in words_list])


def build_word_cloud(words):
	global mask_file, dictionary, background, pixel_width, pixel_height, max_font
	stopwords = nltk.corpus.stopwords.words(dictionary)
	
	if mask_file == "":
		mask = np.fromfunction(lambda i, j: (i >= int(pixel_height)) * (j >= int(pixel_width)), (int(pixel_height), int(pixel_width)), dtype=int)
	else:
		mask = np.array(Image.open(mask_file))
		
	word_cloud = WordCloud(width= int(pixel_width), height= int(pixel_height),
	   max_font_size = int(max_font), 
       background_color=background, 
       mask=mask, 
       stopwords=stopwords, 
       max_words=1000,
       contour_color='#023075',
       contour_width=0, 
       collocations = False,
       colormap='Set2').generate(words)
		
	return word_cloud


def plot_image(word_cloud):
	global width, height
	plt.figure(figsize=(int(width),int(height)), frameon=False)
	plt.imshow(word_cloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()


def help():
	print("\nWord Cloud Generator")
	print("Usage: command + option + value")
	print("Example: wcloud -f content.txt\n")
	print("-f  |  filename      Text filename supporting .txt or .pdf files")
	print("-vw |  width         Word cloud image width, default is 15")
	print("-vh |  height        Word cloud image height, default is 9")
	print("-pw |  pixelWidth    Word cloud pixel width, default is 800")
	print("-ph |  pixelHeight   Word cloud pixel height, default is 500")
	print("-mf |  maxFont	    Max font size, default is 110")
	print("-m  |  mask          Image file mask must be white background and black foreground supports .jpg or .png files")
	print("-s  |  stopwords     NLTK stopwords dictionary. Example english, portuguese, french... default is english")
	print("-b  |  background    Word Cloud background. white, black and etc.. default is black")
	print("-h  |  help          Display this options\n")


def options():
	global text_file, file_extension, mask_file, background, dictionary, width, height, pixel_width, pixel_height, max_font
	if len(sys.argv) > 1:
		for n in range(1, len(sys.argv)):
			if sys.argv[n] == "-f" or sys.argv[n] == "filename":
				text_file = sys.argv[n+1]
				filepath, file_extension = os.path.splitext(text_file)
			elif sys.argv[n] == "-vw" or sys.argv[n] == "width":
				width = sys.argv[n+1]
			elif sys.argv[n] == "-vh" or sys.argv[n] == "height":
				height = sys.argv[n+1]
			elif sys.argv[n] == "-pw" or sys.argv[n] == "pixelWidth":
				pixel_width = sys.argv[n+1]
			elif sys.argv[n] == "-ph" or sys.argv[n] == "pixelHeight":
				pixel_height = sys.argv[n+1]
			elif sys.argv[n] == "-mf" or sys.argv[n] == "maxFont":
				max_font = sys.argv[n+1]
			elif sys.argv[n] == "-m" or sys.argv[n] == "mask":
				mask_file = sys.argv[n+1]
			elif sys.argv[n] == "-s" or sys.argv[n] == "stopwords":
				dictionary = sys.argv[n+1]
			elif sys.argv[n] == "-b" or sys.argv[n] == "background":
				background = sys.argv[n+1]
			elif sys.argv[n] == "-h" or sys.argv[n] == "help":
				help()
	else:
		print("\nMissing arguments, add help or -h to see options\n")


def start():
	options()
	if text_file != "" and file_extension != "":
		if (file_extension.lower() == ".pdf"):
			words_list = build_words_list(read_text_from_pdf(text_file))
		else:
			words_list = build_words_list(read_file(text_file))
		words_counter = len(set(words_list))
		print(f"Document has {words_counter} different words")
		print("Building a WordCloud...")
		plot_image(build_word_cloud(get_words_from_list(words_list)))


start()
