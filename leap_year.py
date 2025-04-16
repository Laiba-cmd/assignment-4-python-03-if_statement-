import streamlit as st

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    st.title("Leap Year Checker")
    
    # Input for the year
    year = st.number_input("Enter a year:", min_value=0)
    
    if st.button("Check Leap Year"):
        if is_leap_year(year):
            st.write(f"{year} is a leap year.")
        else:
            st.write(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
