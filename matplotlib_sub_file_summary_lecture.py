# -----------------------------------------------------------
# Matplotlib Complete Summary Script
# Covers: Line Plot, Sine/Cosine, Scatter, Bar, Histogram,
# Subplots, Axis Controls, Styles, and Annotations.
# -----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ===========================================================
# 1. BASIC LINE PLOT
# ===========================================================

# Creating simple data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Plotting a basic line graph
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# ===========================================================
# 2. SINE & COSINE WAVES
# ===========================================================

# Creating smooth values from 0 to 10
x = np.linspace(0, 10, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plotting sine and cosine
plt.plot(x, y_sin, label="Sine", linewidth=2)
plt.plot(x, y_cos, label="Cosine", linewidth=2)
plt.title("Sine & Cosine Waves")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)       # Turns on the grid
plt.legend()         # Shows line labels
plt.show()


# ===========================================================
# 3. CUSTOM LINE STYLES, COLORS, MARKERS
# ===========================================================

plt.plot(x, y_sin, color='red', linestyle='--', linewidth=2, marker='o', label="Sine")
plt.plot(x, y_cos, color='blue', linestyle='-', linewidth=1, marker='^', label="Cosine")
plt.title("Custom Line Styles")
plt.legend()
plt.grid(True)
plt.show()


# ===========================================================
# 4. SCATTER PLOT
# ===========================================================

plt.scatter(x, np.sin(x), color='green', marker='x', s=50)
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("sin(X)")
plt.show()


# ===========================================================
# 5. BAR CHART
# ===========================================================

labels = ["A", "B", "C", "D"]
values = [4, 7, 1, 8]

plt.bar(labels, values, color='purple')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


# ===========================================================
# 6. HISTOGRAM
# ===========================================================

data = np.random.randn(1000)   # 1000 random values (normal distribution)

plt.hist(data, bins=30, color="orange")
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# ===========================================================
# 7. SUBPLOTS (MULTIPLE CHARTS IN ONE FIGURE)
# ===========================================================

plt.figure(figsize=(10, 5))        # Width=10, Height=5 inches

# First subplot (left)
plt.subplot(1, 2, 1)               # (rows=1, cols=2, position=1)
plt.plot(x, y_sin)
plt.title("Sine Wave")

# Second subplot (right)
plt.subplot(1, 2, 2)               # position=2
plt.plot(x, y_cos)
plt.title("Cosine Wave")

plt.show()


# ===========================================================
# 8. AXIS LIMITS
# ===========================================================

plt.plot(x, y_sin)
plt.title("Axis Limits Example")
plt.xlim(0, 10)     # Limit X-axis
plt.ylim(-1, 1)     # Limit Y-axis
plt.grid(True)
plt.show()


# ===========================================================
# 9. ANNOTATIONS (ADDING TEXT & ARROWS)
# ===========================================================

plt.plot(x, y_sin)
plt.title("Annotated Sine Wave")
plt.annotate("Peak Here",
             xy=(np.pi/2, 1),           # Point to mark
             xytext=(3, 1.3),           # Text location
             arrowprops=dict(arrowstyle="->"))

plt.show()


# ===========================================================
# 10. STYLES (THEMES)
# ===========================================================

plt.style.use("ggplot")     # Applying a style theme

plt.plot(x, y_cos, linewidth=2)
plt.title("Styled Chart using ggplot")
plt.show()

# Reset style to default
plt.style.use("default")
