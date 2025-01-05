import streamlit as st
st.title("🎈 Comoara fermecata")
st.write(
    "\n🍕Welcome to Python Pizza Deliveries!🍕\n"
)
print("\n🍕Welcome to Python Pizza Deliveries!🍕\n")
size = input("What size pizza do you want? S, M or L: ")
if size == "M":
    pizza1 = 20
if size == "S":
    pizza1 = 15
if size == "L":
    pizza1 = 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni  == "Y":
    if size == size == "M":
        pizza1 += 2
    elif size == "S":
        pizza1 += 2
    elif size == "L":
        pizza1 += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pizza1 += 1
print(f"Your final bill is: ${pizza1}.")
