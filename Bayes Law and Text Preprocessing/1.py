import numpy as np
import pandas as pd
import hazm as hz
import math

train_data = pd.read_csv(r"c:\Users\Asus\Desktop\university\term 3\آمار و احتمال\CA0\books_train.csv")
test_data = pd.read_csv(r"c:\Users\Asus\Desktop\university\term 3\آمار و احتمال\CA0\books_test.csv")

numbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
puncts = ['!', '`', '@', '#', '%', '^', '&', '*', '(', ')', '…', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '\'', '\"', ',', '<', '>', '/', '؟', '.', '،', '؛', '«', '»']

normalize_obj = hz.Normalizer()
tokenize_obj = hz.WordTokenizer()
lemmatize_obj = hz.Lemmatizer()
stop_words = hz.stopwords_list()

all_unique_words = []

def remove_puncts_and_nums(text):
    new_text = ""
    for char in text:
        if (char not in puncts) and (char not in numbers):
            new_text += char
    return new_text
            
def remove_stop_words(words_list):
    new_words = []
    for i in range(len(words_list)):
        if words_list[i] not in stop_words:
            new_words.append(words_list[i])
    return new_words

def lemmatizer_func(words_list):
    new_words = []
    for i in range(len(words_list)):
        new_words.append(lemmatize_obj.lemmatize(words_list[i]))
    return new_words

def sort_words(data, type):      
    for i in range(len(data)):
        normalized_title = normalize_obj.normalize(data.loc[i]["title"])
        normalized_description = normalize_obj.normalize(data.loc[i]["description"])
        
        final_normalized_title = remove_puncts_and_nums(normalized_title)
        final_normalized_description = remove_puncts_and_nums(normalized_description)
        
        tokenized_title = tokenize_obj.tokenize(final_normalized_title)
        tokenized_description = tokenize_obj.tokenize(final_normalized_description)
        
        lemmatized_title = lemmatizer_func(tokenized_title)
        lemmatized_description = lemmatizer_func(tokenized_description)
        
        data.loc[i]["title"] = remove_stop_words(lemmatized_title)
        data.loc[i]["description"] = remove_stop_words(lemmatized_description)
        
        if (type == "train"):
            all_unique_words.extend(data.loc[i]["title"] + data.loc[i]["description"])
                                
sort_words(train_data, "train")
sort_words(test_data, "test")

all_unique_words = list(set(all_unique_words))

BoW = [{}, {}, {}, {}, {}, {}]

for i in range(len(BoW)):
    for word in all_unique_words:
        BoW[i][word] = 0.1
        
def set_words_in_bow(words, category):
    for word in words:
        if (category == "رمان"): BoW[0][word] = BoW[0].get(word) + 1
        elif (category == "مدیریت و کسب و کار"): BoW[1][word] = BoW[1].get(word) + 1
        elif (category == "کلیات اسلام"): BoW[2][word] = BoW[2].get(word) + 1
        elif (category == "داستان کودک و نوجوانان"): BoW[3][word] = BoW[3].get(word) + 1
        elif (category == "داستان کوتاه"): BoW[4][word] = BoW[4].get(word) + 1
        elif (category == "جامعه‌شناسی"): BoW[5][word] = BoW[5].get(word) + 1
    

for i in range(len(train_data)):
    category = train_data.loc[i]["categories"]
    words = train_data.loc[i]["title"] + train_data.loc[i]["description"]
    set_words_in_bow(words, category)

def number_of_words_of_a_category(category_index):
    sum = 0
    for num in BoW[category_index].values():
        sum += num
    return sum

def compute_probability_of_a_category(description):
    max_probability = -1000000
    for category_index in range(len(BoW)):
        temp_probability = 0
        for word in description:
            if (word in BoW[category_index]):
                prob = float(BoW[category_index].get(word)) / float(number_of_words_of_a_category(category_index))
                temp_probability += math.log10(prob)
        
        if (temp_probability > max_probability):
            max_probability = temp_probability
            if (category_index == 0): cat = "رمان"
            elif (category_index == 1): cat = "مدیریت و کسب و کار"
            elif (category_index == 2): cat = "کلیات اسلام"
            elif (category_index == 3): cat = "داستان کودک و نوجوانان"
            elif (category_index == 4): cat = "داستان کوتاه"
            elif (category_index == 5): cat = "جامعه‌شناسی"
            
    return cat
    
number_of_correct_categories = 0

for i in range(len(test_data)):
    description = test_data.loc[i]["description"]
    orginal_category = test_data.loc[i]["categories"]
    test_category = compute_probability_of_a_category(description)

    if (orginal_category == test_category): number_of_correct_categories += 1

print((number_of_correct_categories / len(test_data)) * 100)