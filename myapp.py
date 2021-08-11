#############################
#   Import Libraries
#############################

import pandas as pd 
import streamlit as st 
import altair as alt 
from PIL import Image

#############################
#   Page Title
#############################

image = Image.open('dna_image.png')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web Application

This app counts the nucleotide composition of DNA queried!

***
""")

#############################
#   DNA Input Text Box
#############################

st.header('Enter DNA sequence here')

sequence_input = ">DNA Query\nGAACACGTGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines() # Splits newlines into a list
sequence = sequence[1:] # Skips the index 0 which is the first item on the list (DNA Query)
sequence = ''.join(sequence) # Concatenates the list to a string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA Nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

##########################################
#   Four ways to display the output below
##########################################

### 1. Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C')),
            ])
    return d 

X = DNA_nucleotide_count(sequence)

X

### 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A) in the DNA sequence.')
st.write('There are ' + str(X['T']) + ' thymine (T) in the DNA sequence.')
st.write('There are ' + str(X['G']) + ' guanine (G) in the DNA sequence.')
st.write('There are ' + str(X['C']) + ' cytosine (C) in the DNA sequence.')

### 3. Display Result as dataframe
st.subheader('3. Display Result as Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart Using Altair')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # This line controls the width of the bar
)
st.write(p)

st.subheader('Completed by Adubi Olubunmi')












