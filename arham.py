if st.button("Save Record"):
    # Insert the record into the database
    c.execute("INSERT INTO records (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    st.write("Record saved successfully!")
