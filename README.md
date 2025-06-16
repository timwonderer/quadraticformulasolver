# Quadratic Formula Solver

_The solver that shows its work._

A **side quest** that got out of hand (again).

This isn’t just another quadratic solver. It’s a deep dive into the **how** behind the formula:

$$
ax^2 + bx + c = 0
$$

$$
a \ne 0
$$

Instead of relying on built-in math functions, this program **rebuilds everything from scratch**. Because **knowing how things work** is half the fun.

> [!NOTE]  
> This isn’t the fastest quadratic solver out there (Python’s built-in math functions still win). But if you’re here for the **process, transparency, and fun**, you’re in the right place.

---

## 🚀 Features

| Feature                    | How It Works                                    |
|----------------------------|-------------------------------------------------|
| 🔍 **Square Root Estimation** | Binary + linear search (no `math.sqrt()`)       |
| ✅ **Radical Simplification** | Prime factorization (Sieve of Eratosthenes)    |
| ⚙️ **Fraction Reduction**     | Custom GCD algorithm                           |
| 🧩 **Complex Root Handling**  | Neatly formatted with `√` and `i` symbols       |

> [!TIP]
>  **Efficiency isn’t just speed**—it’s knowing **why each step exists**.
> This program breaks down the process of solving quadratic equation into painfully
> detailed steps

---

## 💡 Example Output

```bash
Enter coefficient 'a': 1
Enter coefficient 'b': 2
Enter coefficient 'c': 3

Solutions for the entered equation:
x = -1+√2i
x = -1-√2i
```

Try something bigger:

```bash
Enter coefficient 'a': 1
Enter coefficient 'b': -1000
Enter coefficient 'c': 1

Solutions for the entered equation:
x = 500+√249999
x = 500-√249999
```

---

### 🛠️ How to Run

#### Console (CLI):

```bash
python main.py
```

---

## 📊 File Map

```
quadratic-solver/
├── main.py                       # CLI app
├── quadratic_function_solver.py  # Core solver (discriminant, radical simplification)
├── integer_square_root_finder.py # Integer square root estimator
├── square_root_simplifier.py     # Prime factorization for simplifying radicals
├── reduce_fraction.py            # GCD + fraction reduction
├── answer_formatter.py           # Formats solutions into readable strings
└── test_quadratic_function_solver.py # Test cases (including edge cases!)
```

---

## Behind the Code

I’m a **teacher**, **problem-solver**, and someone who enjoys asking, **"But what if I did it differently?"**

This solver isn’t about reinventing the wheel. It’s about **taking the wheel apart** to see how it works—and maybe putting it back together better (or at least more thoughtfully).

In the classroom, I encourage students to **explore how things work**, not just **accept the answer**. That same spirit guides my programming. I don’t write code like this because it’s needed—I write code like this because:

- **Efficiency** isn’t just about speed—it’s about **understanding each piece** and making sure it earns its place.
- **Complexity** can be beautiful if it helps reveal **why** something works.

This project grew from the same curiosity that led me to build an **integer square root finder** during a break. I could’ve used Python’s built-in functions. But I’m the kind of person who **solves non-problems for fun**—just to see what I learn along the way.

### A quick story:

When I built the **integer square root finder**, it started as a side project to optimize my **prime checker** (which, let’s be honest, wasn’t all that reliable). I found myself obsessing over whether I could **narrow the search range** for square roots based on **digit patterns**—counting digits, spotting trends, and asking **“Is there a mathematical rule I’m missing?”** Three days later, I had something efficient enough to **check for integer square roots** without crashing my machine.

This quadratic solver? It’s the **natural next step**. If I’m going to **simplify square roots**, I might as well **build the whole formula** from the ground up.

That’s just how my brain works.

> [!IMPORTANT]
> This project is for **learning and exploration**. It’s not optimized for production use or industrial-strength number crunching. But it will show you **how things work** under the hood.

---

## License
This project is licensed under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0/).

>[!IMPORTANT]
> **This license allows you to:**
> - Use this project in classrooms, clubs, and nonprofit educational settings
> - Modify or adapt it for school use, assignments, or personal learning
> - Share it with students or other educators
> - Use it for research or academic presentations (as long as they are not sold)
> 
> **This license prohibits you to:**
> - Use it as part of a commercial product or SaaS platform
> - Host a paid service or subscription that includes this software
> - Incorporate it into any offering that generates revenue (e.g., paid courses, tutoring platforms)
> - Use it internally within a for-profit business, even if not publicly distributed
