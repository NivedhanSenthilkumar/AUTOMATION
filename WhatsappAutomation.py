'SINGLE MESSAGE'
import pywhatkit
pywhatkit.sendwhatmsg('+919790766998','HI',12,19)

'BULK MESSAGES'
# Program to send bulk customized message through WhatsApp web application
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas
import time

# Load the chrome driver
driver = webdriver.Chrome('/path/to/chromedriver')
count = 0

# Open WhatsApp URL in chrome browser
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

# Read data from excel
excel_data = pandas.read_excel('D:/Customer bulk email data.xlsx', sheet_name='Customers')

# Iterate excel rows till to finish
for column in excel_data['Name'].tolist():
    # Assign customized message
    message = excel_data['Message'][0]

    # Locate search box through x_path
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(lambda driver:driver.find_element_by_xpath(search_box))

    # Clear search box if any contact number is written in it
    person_title.clear()

    # Send contact number in search box
    person_title.send_keys(str(excel_data['Contact'][count]))
    count = count + 1

    # Wait for 2 seconds to search contact number
    time.sleep(2)

    try:
        # Load error message in case unavailability of contact number
        element = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
    except NoSuchElementException:
        # Format the message from excel sheet
        message = message.replace('{customer_name}', column)
        person_title.send_keys(Keys.ENTER)
        actions = ActionChains(driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()

# Close chrome browser
driver.quit()

import regex as re
import pandas as pd
import numpy as np
import emoji
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import emoji


def identify_Start(s):
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result = re.match(pattern, s)
    if result:
        return True
    return False


def get_Authors(s):
    s = s.split(":")
    if len(s) == 2:
        return True
    else:
        return False


def get_msg(line):
    try:
        splitLine = line.split('-')
        datetime = splitLine[0].split(',')
        date = datetime[0].replace('[', '')
        time = datetime[1]
        chat_line = splitLine[1]
        chat_line = chat_line.split(':')
        author = chat_line[0].strip()
        message = chat_line[1]
        return date, time, author, message
    except:
        return 'null', 'null', 'Reply', line


def extract_emojis(s):
    return ''.join(c for c in s if c in emoji.UNICODE_EMOJI)


conversation = 'jaffarston.txt'
with open(conversation, encoding="utf-8") as fp:
    chat = []
    fp.readline()
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        date, time, author, message = get_msg(line)
        chat.append([date, time, author, message])
    df = pd.DataFrame(chat, columns=['Date', 'Time', 'Author', 'Message'])
    df = df[~df.Message.str.contains("Media")]
    df = df[~df['Message'].isin(['Media'])]
    print(df.tail(20))
    print("Authors of the chat = ", df.Author.unique())
    df['Emojis'] = df["Message"].apply(extract_emojis)
    Emojis = sum(df['Emojis'].str.len())
    print("Total messages in the chat", df.shape[0])
    print("Total Number of emoji's used in the chat", Emojis)
    df['Letter_Count'] = df['Message'].apply(lambda s: len(s))
    df['Word_Count'] = df['Message'].apply(lambda s: len(s.split(' ')))
    for i in df.Author.unique():
        print('\n')
        req_df = df[df["Author"] == i]
        print("Messages sent by ", i, req_df.shape[0])
        words_per_message = round((np.sum(req_df['Word_Count'])) / req_df.shape[0], 3)
        print("Words per message of ", i, words_per_message)
        emojis = sum(req_df['Emojis'].str.len())
        print('Emojis Sent by ', i, emojis)
    total_emojis_list = list([a for b in df.Emojis for a in b])
    emoji_dict = dict(Counter(total_emojis_list))
    emoji_dict = sorted(emoji_dict.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    for i in emoji_dict:
        print(i, end=" ")

    text = " ".join(review for review in df.Message)

    stopwords = set(STOPWORDS)
    stop_words = {'I', 'will', 's', 'You', 'da', 'It', 'What', 'We', 'Shyam', 'Aishwarya', 'No', 'm', 's', 'time',
                  'now', 't', 'So', 'https', 'group', 'Sneha', "'s", 'okay', 'one', "n't", 'Good', 'tell', 'want',
                  'come', 'tomorrow', 'don', 'know', 'changed', 'think', 'This', 'Yashita', 'Go', 'Guy', 'Aswin',
                  'Team', 'yeah', 'size', 'night', 'Why', 'Okay', 'need', 'go', 'going', 'Yeah', 'For', 'icon',
                  'The', 'coming', 'home', 'guys', 'But', "'ll", "please", "send", "Cool", "next"}
    stopwords.update(stop_words)
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stopwords]
    filtered_sentence = ' '.join(filtered_sentence)
    filtered_sentence = re.sub(r"[^\w\d'\s]+", '', filtered_sentence)
    c = Counter(filtered_sentence.split())
    print(c.most_common(20))
    print("There are {} words in all the messages.".format(len(text)))
    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    # Display the generated image:
    # the matplotlib way:
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()