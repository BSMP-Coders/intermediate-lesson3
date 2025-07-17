# 🐢 Week 3, Lesson 1: Build a Python Turtle Game with GitHub Copilot

## Welcome to your first game with Turtle!

You're about to dive into **Turtle**, a built-in Python library that helps you create simple, fun games with colorful graphics using just code! This lesson will guide you step-by-step to bring your ideas to life and share them with others.

## 🎯 What You'll Do

By the end of this lesson, you'll be able to:

- **Create your first animated game** - Build a working game using Python Turtle and GitHub Copilot
- **Master GitHub collaboration** - Share your project and give feedback like a pro developer

## 🛠️ Setup Checklist

This time, you’ll be working locally instead of in the cloud. That means using Visual Studio Code and cloning your project to your own computer.

**Step 1: Get Python**

- Go to the Windows Store and install **Python 3.13**
- OR open the command line and type `python` (it'll take you to the installation page automatically!)

**Step 2: Download Your Code Editor**

- Download and install **Visual Studio Code** from the Windows Store

**Step 3: Connect to Your Project**

- Open Visual Studio Code
- Go to **Source Control** > **Clone** (under the three dots)
- Follow the instructions to fork and clone the repository

**Step 4: Add Your AI Coding Assistant**

- In VS Code, click the Extensions icon
- Search for **"GitHub Copilot"** and install it

**Step 5: Add Python Support**

- Still in Extensions, search for **"Python"** and install it

**Step 6: Test Everything Works**

- Open the terminal in Visual Studio Code
- Type `python` and press Enter
- If you see Python starting up — you’re good to go!



> No extra installs needed — Turtle comes built into Python!

## 🐢 Learn the Basics of Turtle

Before you build your own game, let’s learn a few basics about how Turtle works in Python. Open `app.py` and follow these steps to try things out.

### 🐢 Step 1: Import and Create a Turtle

```python
import turtle

wn = turtle.Screen()  # Creates the game window
player = turtle.Turtle()  # Creates a turtle
```

### 🎨 Step 2: Customize the Turtle

```python
player.shape("turtle")     # Changes the shape
player.color("blue")       # Changes the color
player.speed(1)            # Sets movement speed
```

### 🔄 Step 3: Move the Turtle Around

```python
player.forward(100)  # Move forward
player.right(90)     # Turn right
player.forward(100)
```

### 🧠 Step 4: Use Functions and Loops

```python
for _ in range(4):
    player.forward(100)
    player.right(90)  # Draws a square
```

### 🕹️ Step 5: Add User Input

```python
def move_up():
    player.setheading(90)
    player.forward(10)

wn.listen()
wn.onkey(move_up, "Up")
wn.mainloop()  # Keeps the window open
```

> Now you're ready to build your own game!

## 🕹️ Choose Your Turtle Game!

Open [app.py](/lesson-2/app.py) and use these prompts with GitHub Copilot. **Important:** Test your game after each prompt to see your progress!

| 🐢 Game                | 🎯 What You'll Build                               | 🚀 Step-by-Step Prompts                                                                                          |
| ---------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **🏃 Dodge the Dots**  | Move your turtle and avoid falling obstacles       | 1. "Draw a turtle and falling dots"2. "Move turtle with arrow keys"3. "End game when turtle hits a dot"          |
| **🍎 Catch the Apple** | Catch falling apples using your turtle as a basket | 1. "Draw a turtle and falling apple"2. "Move turtle left/right"3. "Detect when turtle catches apple"             |
| **💥 Turtle Chase**    | Chase and tag a moving target using your turtle    | 1. "Draw two turtles"2. "Make one move randomly"3. "Move the player turtle with arrow keys and detect collision" |
| **🧱 Simple Breakout** | Break a wall of bricks with a bouncing turtle ball | 1. "Draw bricks, paddle, and turtle ball"2. "Bounce turtle off paddle"3. "Remove bricks when hit"                |

> **💡 Pro Tip:** Turtle is slower than Pygame, but great for beginners. Run your game after each change to see it evolve!

## How to run your game

You have two easy options:

### ▶️ Option 1: Use the Play Button in VS Code

- Open `app.py`
- Click the green **Run** or **Play** button in the top right corner
- Your game will open in a new window!

### 💻 Option 2: Use the Terminal

In the terminal, type the following commands:

```bash
cd lesson-2
python app.py
```

## 🔎 Share, Collaborate, and Review in GitHub

Just like real developers, you’ll use GitHub to share, improve, and review your code.

### Step 1: Commit & Push Your Game in the Editor

1. Open the Source Control panel in VS Code. You should see your changes listed.
2. Add a message like: "First version of my Turtle game".
3. Click Commit and then Sync to upload your code.

### Step 2: Try Someone Else's Game

1. Ask a classmate for their GitHub repo link.
2. Clone it using VS Code.
3. Open and play their game.
4. Take notes on what works well and what could be improved.

### Step 3: Leave Feedback via GitHub Issues

1. On their GitHub page, click the **Issues** tab → **New Issue**.
2. Write clear, helpful feedback in the Description.
3. Use the Title to briefly summarize your comment.

> Feedback is how real teams improve! Be kind, be honest, be specific.