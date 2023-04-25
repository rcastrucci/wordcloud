# Word Cloud Generator

This python script generates a word cloud out of text files or pdf files.

Some customizations can be done by the arguments on prompt no need to touch the code.

Dependencies needed:
python 3.10
nltk
pypdf2
wordcloud

### Clone this repository and give executable permission to the file wcloud.py
    chmod +x wcloud.py

### To Use
    ./wcloud.py help
    
Word Cloud Generator<br>
Usage: command + option + value<br>
Example: wcloud -f content.txt<br>
<br>
<ul>
<li>-f Text filename supporting .txt or .pdf files</li>
<li>-vw Word cloud image width, default is 15</li>
<li>-vh Word cloud image height, default is 9</li>
<li>-pw Word cloud pixel width, default is 800</li>
<li>-ph Word cloud pixel height, default is 500</li>
<li>-mf Max font size, default is 110</li>
<li>-m Image file mask must be white background and black foreground supports .jpg or .png files</li>
<li>-s NLTK stopwords dictionary. Example english, portuguese, french... default is english</li>
<li>-b Word Cloud background. white, black and etc.. default is black</li>
<li>-h Display this options</li>
</ul>
