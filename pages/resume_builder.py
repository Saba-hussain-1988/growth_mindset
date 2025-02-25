import streamlit as st

st.title("Resume Builder")
st.image("images\sr.jpg")

# Function for education information
def get_education_information():
    """Function to collect educational information from user"""
    education_list = []  # List to store multiple education records
    num_entries = st.number_input("How many education records do you want to enter?", min_value=1, max_value=20, step=1)

    for i in range(num_entries):
        st.write(f"### Education Entry {i+1}")
        certificate = st.text_input(f"Certificate/Degree {i+1}", key=f"cert_{i}")
        institute = st.text_input(f"Institute Name {i+1}", key=f"inst_{i}")
        year = st.number_input(f"Year of Completion {i+1}", min_value=1920, max_value=2025, step=1, key=f"year_{i}")

        if certificate and institute and year:  # Ensure all fields are filled
            education_list.append({
                "Certificate": certificate,
                "Institute": institute,
                "Year": year
            })

    return education_list  # Return the collected data


# function personal information
def get_personal_information():
    name = st.text_input("Full Name").title() # capitalize the very first letter of each word.
    contact = st.text_input("Contact Number")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=13, max_value=70, step=1)
    # Gender selection
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    
    city = st.text_input("City").title()

    return name, contact, email, age, gender, city



# Create a form
with st.form(key="user_form"):
    st.subheader("Personal Information")
    name, contact, email, age, gender, city = get_personal_information()

    st.subheader("Academic Information")
    education_data = get_education_information()

    # Submit button
    submit_button = st.form_submit_button("Submit")
    # st.success("Form Submitted Successfully!")

# Process form submission
if submit_button:
    if name and contact and email and age and gender and city and education_data:
    
        st.subheader("Personal Information")
        st.write(f"**Name:** {name}")
        st.write(f"**Contact:** {contact}")
        st.write(f"**Email:** {email}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**City:** {city}")
        st.write()
        st.subheader("Academic Information")
        for idx, edu in enumerate(education_data, 1):
                st.write(f"**{idx}. {edu['Certificate']}** from {edu['Institute']} in {edu['Year']}")
        
    else:
        st.error("❌ Please fill all fields!")
