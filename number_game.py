import streamlit as st
import random

st.set_page_config(page_title="🎮 Number Guessing Game", layout="centered")

st.title("🎯 Guess the Number 2.0")
st.markdown("Guess a number between **1 and 100**!")

# Initialize game state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.score = 0

# Input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.tries += 1

    if guess == st.session_state.number:
        st.success(f"🎉 Correct! The number was {st.session_state.number}.")
        st.balloons()
        st.session_state.score += 1
        st.markdown(f"✅ **Score:** {st.session_state.score} | 🧠 Tries: {st.session_state.tries}")
        st.session_state.number = random.randint(1, 100)
        st.session_state.tries = 0  # reset tries for new round
    elif guess < st.session_state.number:
        st.warning("📉 Too low! Try a higher number.")
    else:
        st.warning("📈 Too high! Try a lower number.")

# Show current score + tries
st.markdown(f"**Current Score:** {st.session_state.score}")
st.markdown(f"**Tries this round:** {st.session_state.tries}")

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.score = 0
    st.success("Game has been reset!")
