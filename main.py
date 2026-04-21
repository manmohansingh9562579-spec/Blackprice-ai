import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

# DARK THEME 🔥
plt.style.use('dark_background')

# Load data
df = pd.read_csv("data.csv")

X = df[["area", "bedrooms", "age"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("🔥 BlackPrice AI Ready 🔥")

# USER INPUT
area = float(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))
age = int(input("Enter house age: "))

prediction = model.predict([[area, bedrooms, age]])

print(f"\n💰 Estimated Price: ₹{prediction[0]:.2f} Lakhs")

# GRAPH ANIMATION 🔥
fig, ax = plt.subplots()
ax.set_title("BlackPrice AI - Data Visualization")
ax.set_xlabel("Area")
ax.set_ylabel("Price")

x_data = []
y_data = []

def update(frame):
    x_data.append(df["area"][frame])
    y_data.append(df["price"][frame])
    
    ax.clear()
    ax.set_title("BlackPrice AI - Animated Graph")
    ax.set_xlabel("Area")
    ax.set_ylabel("Price")
    
    ax.scatter(x_data, y_data, color='white')
    ax.plot(x_data, y_data)

ani = FuncAnimation(fig, update, frames=len(df), interval=800)

plt.show()