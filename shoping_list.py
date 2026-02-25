shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]

# task 1
shopping_list.append({"item": "Butter", "price": 80})
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)
print(len(shopping_list))

# task 2
total_price = sum(item["price"] for item in shopping_list)
print("Total price:", total_price)
most_expensive_item = max(shopping_list, key=lambda x: x["price"])
print("Most expensive item:", most_expensive_item["item"], "with price", most_expensive_item["price"])
total_cost = sum(item["price"] for item in shopping_list)
print("Total cost of items in the shopping list:", total_cost)

# task 3
summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": round(total_cost / len(shopping_list), 2)
    }
print("Summary:", summary)