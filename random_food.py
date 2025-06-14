import random
import argparse

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

def pick_foods(foods, count=1):
    """Return `count` random foods from the provided list."""
    if count <= len(foods):
        return random.sample(foods, k=count)
    return [random.choice(foods) for _ in range(count)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="랜덤 음식 추천기")
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1,
        help="추천 받을 음식 개수 (기본값: 1)",
    )
    parser.add_argument(
        "--foods",
        help="쉼표로 구분된 추가 음식 목록",
    )
    args = parser.parse_args()

    food_list = FOODS.copy()
    if args.foods:
        extras = [f.strip() for f in args.foods.split(",") if f.strip()]
        food_list.extend(extras)

    for food in pick_foods(food_list, args.num):
        print("오늘의 추천 음식:", food)
