import streamlit
streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')

streamlit.text ('đĨŖ Omega 3 & Blueberry Oatmeal')

streamlit.text('đĨŦ Kale, Spinich and Rocket Smoothie')

streamlit.text('đ Hard Boiled Free_Range Eggs')

streamlit.text ('đĻģ đ  Avocado Toast')

streamlit.header ('đđ Build Your Own Fruit Smoothie đĨđ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

 
