import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from preprocess import *
import random
import nltk
from translate import Translator

nltk.download('stopwords')

# Define the possible emotions
emotions = ['mutlu','üzüntü', 'kızgınlık', 'neşe', 'korkmak', 'şaşkın', 'kıskanç', 'heyecanlı', 'inatçı']

# Function to get user input
def user_input():
    text = st.sidebar.text_input('Buraya giriniz: ')
    return text

# Function to randomly select an emotion
def random_emotion():
    return random.choice(emotions)

def fromEn_tr_method(input):
    translator = Translator(to_lang="tr", from_lang="en")
    tansalte_text = translator.translate(input)
    return tansalte_text

def fromTr_en_method(input):
    translator = Translator(to_lang="en", from_lang="tr")
    tansalte_text = translator.translate(input)
    return tansalte_text

def main():
    st.sidebar.header('Tahminin cümlenizi yazınız')
    
    # Get user input
    input_text_user = user_input()
    input_text = fromTr_en_method(input_text_user)


    # Load the encoder and CountVectorizer
    encoder = pickle.load(open('encoder.pkl', 'rb'))
    cv = pickle.load(open('CountVectorizer.pkl', 'rb'))

    # Load the model
    model = tf.keras.models.load_model('my_model.h5')

    # Preprocess the input
    processed_input = preprocess(input_text)

    # Transform the input text to the format the model expects
    array = cv.transform([processed_input]).toarray()

     # Make a prediction
    pred = model.predict(array)
    predicted_emotion_index = np.argmax(pred, axis=1)
    predicted_emotion = encoder.inverse_transform(predicted_emotion_index)[0]
    prediction_probability = np.max(pred) * 100 



    prediction_text_translate = fromEn_tr_method(predicted_emotion)

    # Display a random emotion
    random_emotion_selected = random_emotion()
    st.subheader('Rastgele Belirlenmiş Duygu')
    st.write(random_emotion_selected)
    

    # Display the prediction
    st.subheader('Duygu Tahmini')
    if input_text == '':
        st.write('Lütfen Metin Giriniz')
    else:
        if random_emotion_selected == prediction_text_translate:
            st.write(f"Girilen Metin: {input_text_user}" )
            st.success(f"Tebrikler, Girdiğiniz duygu: {prediction_text_translate} ile  Seçilen Duygu: {random_emotion_selected} uyuşuyor.")
            st.write("Doğruluk değeri: ",prediction_probability)
            
        else:
            st.write(f"Girilen Metin: {input_text_user}" )
            st.warning(f"{prediction_text_translate} - sizin duygunuz ile eşleşmiyor")
            st.write("Doğruluk değeri: ",prediction_probability)
            

if __name__ == "__main__":
    main()