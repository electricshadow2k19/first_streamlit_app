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

#display the table on the page
#streamlit.dataframe(my_fruit_list)


#Lets put a pick list here so they can pick the fruit they want to include : selct by fruit name
fruits_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
#streamlit.text(fruityvice_response.json())

#normalize json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
