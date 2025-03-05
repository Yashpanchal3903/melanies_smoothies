# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col




st.title("🥤 Customize Your Smoothie! 🥤")


st.write(
    f"""Choose the fruits you want in your custom  Smoothie!: """)


name_on_order = st.text_input("Name of the Smoothie")
st.write("The name of your  Smoothie will be ", name_on_order)

cnx =st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ingredients_list = st.multiselect('Choose up to 5 ingredients :',
                                  my_dataframe,
                                 max_selections=5)

if ingredients_list:
           
            ingredients_string =''
            for fruit_chosen in ingredients_list:
                ingredients_string+=fruit_chosen + ' '
                #st.write(ingredients_string)

            my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
                        values ('""" + ingredients_string + """,'"""+name_on_order+"""')"""
      
    
            Submitted = st.button('Submit ')
            if Submitted:
                st.success('Someone clicked the button', icon = '👍')

my_dataframe = session.table("SMOOTHIES.PUBLIC.ORDERS").filter(col("ORDER_FILLED") == False).collect()



editable_df = st.data_editor(my_dataframe)



            
