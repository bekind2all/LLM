import random

FOODS = [
    "김치볶음밥",
    "라면",
    "피자",
    "햄버거",
    "스시",
    "비빔밥",
    "파스타",
    "치킨",
    "토스트",
    "샐러드",
]

if __name__ == "__main__":
    print("오늘의 추천 음식:", random.choice(FOODS))
