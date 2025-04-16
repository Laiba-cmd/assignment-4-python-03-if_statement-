import streamlit as st
import random

def generate_random_error():
    """Generate a random error message."""
    errors = [
        "ValueError: Invalid value provided.",
        "TypeError: Unsupported operation for the given type.",
        "IndexError: List index out of range.",
        "KeyError: Key not found in the dictionary.",
        "ZeroDivisionError: Division by zero.",
        "AttributeError: 'NoneType' object has no attribute.",
    ]
    return random.choice(errors)

def main():
    st.title("Random Error Generator")
    
    if st.button("Generate Random Error"):
        error_message = generate_random_error()
        st.error(error_message)

if __name__ == "__main__":
    main()
