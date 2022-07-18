import streamlit as st 
import mysql.connector

st.title('This is a SOW form')

with st.form(key='sow-form'):

    project_name = st.text_input('Project Name')

    manager_name = st.text_input('Manager Name')

    available = st.radio(
        "What's your availability",
        ('Yes', 'No', 'Maybe'))

    st.write('Press submit to update')

    submit = st.form_submit_button('Submit')



if project_name is None or manager_name is None or available is None:
    print("Cannot update Null values")

if submit:
#Connecting to Local Database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='uday44_mysql',
        database='mydb',
        charset = 'utf8',
        auth_plugin='mysql_native_password')


    if mydb.is_connected():
                mycursor = mydb.cursor()
                sql = "INSERT INTO sow (project_name, manager_name,available) \
                        VALUES (%s, %s, %s)"
                val = (project_name, manager_name,available)
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.close()
    else:
        print("Database Not Connected")
        #Closing Database connection after writing the data.

    mydb.close()

print("Insertion Successful")
