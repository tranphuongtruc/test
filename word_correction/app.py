import time
import streamlit as st 
from Week_2 import levenshtein_distance
from load_file import load_vocab



def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')
    # load file vocab.txt
    vocabs = load_vocab(file_path='./Data/vocab.txt')      
    
    if st.button("Compute"):
        
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
            
        # sorted by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        
        with st.spinner('Wait for it...'):
            time.sleep(3)
        st.success('Done!')
        st.write('Correct word: ', correct_word)
        
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distances)
        
        st.balloons()
        
if __name__ == "__main__":
    main()
        
        
           