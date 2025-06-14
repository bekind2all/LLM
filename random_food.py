import streamlit as st
import random

FOODS = [
    "김치볶음밥", "보쌈", "피자", "된장찌개",
    "순대국", "샐러드", "파스타", "돈까스", "쌀국수"
]

st.title("🍱 오늘의 점심 메뉴 추천기")

if st.button("메뉴 추천 받기"):
    choice = random.choice(FOODS)
    st.success(f"👉 오늘의 추천 메뉴: **{choice}**")
