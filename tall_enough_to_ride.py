import streamlit as st

def main():
    st.title("Tall Enough to Ride Checker")
    
    # Input for user's height in centimeters
    height = st.number_input("Enter your height (in cm):", min_value=0)
    
    # Define the minimum height requirement for the ride
    min_height = 120  # Example minimum height in cm
    
    if st.button("Check Height Requirement"):
        if height >= min_height:
            st.write("You are tall enough to ride!")
        else:
            st.write("Sorry, you are not tall enough to ride.")

if __name__ == "__main__":
    main()
