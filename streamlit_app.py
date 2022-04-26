import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#import requests
#streamlit.header('FruityVice Fruit Advice')
#fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
# streamlit.write('The user entered', fruit_choice)
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# #streamlit.text(fruityvice_response.json())

# #normalize json
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# streamlit.dataframe(fruityvice_normalized)
# streamlit.stop()
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#       streamlit.error("Please select a fruit to get information.")
#   else:
#       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#       streamlit.dataframe(fruityvice_normalized)
      
# except URLError as e:
#   streamlit.error()
      

def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

streamlit.header('FruityVice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      
except URLError as e:
  streamlit.error()

#streamlit.stop()



#import snowflake.connector

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# #my_data_row = my_cur.fetchone()
# #streamlit.text("Hello from Snowflake :")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains :")
# streamlit.dataframe(my_data_rows)

# add_my_fruit = streamlit.text_input('What fruit would you like to add?', '')
# streamlit.write('The user entered', add_my_fruit)

# my_cur.execute("insert into fruit_load_list values('from steamlit')")



streamlit.header("The fruit load list contains :")
def get_fruit_load_list():
      with my_cnxcursor() as my_cur:
            my_cur.execute("select * from fruit_load_list")
            return my_cur.fetchall()
      
if streamlit.button('Get fruit load list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)













