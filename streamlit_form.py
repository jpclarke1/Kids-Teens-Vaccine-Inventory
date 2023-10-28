import streamlit as st
import sqlite3

# Function to create the SQLite database if it doesn't exist
def create_database():
    conn = sqlite3.connect("vaccine_inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS VACCINES (
            ID INTEGER PRIMARY KEY,
            LOCATION TEXT NOT NULL,
            VACCINE_NAME TEXT NOT NULL,
            LOT_NUMBER TEXT,
            EXPIRATION_DATE DATE
        );
    """)
    conn.commit()
    conn.close()

create_database()

# Streamlit app code
st.title("Vaccine Inventory Management")

location = st.selectbox("Location", ["Northridge", "West Hills", "Pasadena", "Van Nuys", "San Fernando", "Agoura Hills", "La Canada", "Whittier", "Beverly Hills", "Glendale", "Canyon Country", "Culver City", "Valencia", "Torrance", "Mission Hills", "Pico Rivera", "Arcadia", "Santa Monica", "Downey", "Tarzana"])

vaccine_names = [
    "DTaP", "DTaP-HepB-IPV", "DTaP-IPV", "DTaP-IPV/Hib", "HepA", "HepB", "Hib", "HPV",
    "IPV", "MCV4", "MenB", "PCV13", "PPSV23", "RV", "Td", "Tdap", "MMR", "MMRV", "VAR"
]

# Create a form for each vaccine
for vaccine_name in vaccine_names:
    st.subheader(vaccine_name)
    lot_number = st.text_input(f"Lot Number for {vaccine_name}")
    expiration_date = st.date_input(f"Expiration Date for {vaccine_name}")

    if st.button(f"Add {vaccine_name}"):
        conn = sqlite3.connect("vaccine_inventory.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO VACCINES (LOCATION, VACCINE_NAME, LOT_NUMBER, EXPIRATION_DATE) VALUES (?, ?, ?, ?)",
                       (location, vaccine_name, lot_number, expiration_date))
        conn.commit()
        conn.close()
        st.success(f"{vaccine_name} data has been added to the database.")