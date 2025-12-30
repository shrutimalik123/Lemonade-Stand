# 🍋 Lemonade Stand Tycoon - Business Simulator

A text-based economic simulation where you run a lemonade business over the course of seven days. Players must manage their starting capital, purchase supplies, and adapt to changing weather conditions to maximize their profits.

This project is a perfect introduction to:
* **Resource Management:** Balancing a budget against inventory needs.
* **Business Logic:** Using the `min()` function to determine production limits (bottlenecks).
* **Randomized Difficulty:** Using `random.choice` and `random.randint` to simulate unpredictable market conditions (weather).
* **Float Formatting:** Displaying currency correctly using Python f-string formatting.

---

## ✨ Features

* **7-Day Gameplay Loop:** A structured "campaign" that tracks progress day by day.
* **Dynamic Market:** Prices for lemons and sugar are fixed, but your ability to sell depends on the weather.
* **Weather System:** * **Sunny:** High demand (up to 20 customers).
    * **Cloudy:** Moderate demand (up to 10 customers).
    * **Rainy:** Low demand (up to 5 customers).
* **Recipe Logic:** Each pitcher requires a 1:1 ratio of lemons to sugar and produces 5 glasses.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `lemonade.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python lemonade.py
    ```

### 3. Gameplay Instructions
1.  **Buying Phase:** Check your cash and inventory, then decide how many supplies to buy. Be careful not to overspend!
2.  **Production:** The computer automatically calculates how many pitchers you can make based on your lowest ingredient count.
3.  **Selling:** The weather is revealed, and customers arrive. Each glass sold earns you $1.50.
4.  **Goal:** Try to end Day 7 with more than your starting $20.00!

---

## 🧠 Code Structure Highlights

### Ingredient Bottlenecks
One of the most important logic pieces in the game is determining how many pitchers you can make. If you have 10 lemons but only 2 bags of sugar, you can only make 2 pitchers. We handle this using `min()`:

```python
# The limiting factor determines production
pitchers = min(inventory_lemons, inventory_sugar)

