import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text""")

def get_data():
    return np.random.randn(10)

@st.cache_data
def get_cached_data():
    return get_data()


def get_list():
    return list(range(1, 11))

@st.cache_data
def get_cached_list():
    return get_list()

df = pd.DataFrame({
    'first column': get_cached_list(),
    'second column': get_cached_data()
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

st.text(f'this is the number of lines: {line_count}')

direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))

if st.checkbox('Show content'):
    st.markdown("this is checked")
