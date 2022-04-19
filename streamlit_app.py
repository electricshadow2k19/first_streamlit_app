import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard boiled eggs')


streamlit.header('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Lets put a pick list here so they can pick the fruit they want to include : selct by fruit name
streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

