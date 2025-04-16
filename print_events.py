import streamlit as st

def main():
    st.title("Event Printer")
    
    # Input for event name
    event_name = st.text_input("Enter the event name:")
    
    if st.button("Print Event"):
        if event_name:
            st.write(f"Event: {event_name}")
        else:
            st.write("Please enter an event name.")

if __name__ == "__main__":
    main()
