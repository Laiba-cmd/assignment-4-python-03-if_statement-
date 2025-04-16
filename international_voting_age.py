import streamlit as st

def main():
    st.title("International Voting Age Checker")
    
    # Input for user's age
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    
    # Voting age criteria for some countries
    voting_ages = {
        "USA": 18,
        "Canada": 18,
        "UK": 18,
        "Germany": 18,
        "Australia": 18,
        "India": 18,
        "Brazil": 16,
        "Japan": 18,
        "South Korea": 18,
        "Sweden": 18
    }
    
    if st.button("Check Voting Eligibility"):
        eligible_countries = [country for country, voting_age in voting_ages.items() if age >= voting_age]
        if eligible_countries:
            st.write(f"You are eligible to vote in the following countries: {', '.join(eligible_countries)}")
        else:
            st.write("You are not eligible to vote in any listed countries.")

if __name__ == "__main__":
    main()
