import streamlit as st
import random

st.title("🎲 Guess the Number Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input("Guess a number between 1 and 10", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    if guess == st.session_state.number:
        st.success("🎉 You guessed it right!")
        st.session_state.number = random.randint(1, 10)  # Reset the game
    else:
        st.error("❌ Nope! Try again.")
