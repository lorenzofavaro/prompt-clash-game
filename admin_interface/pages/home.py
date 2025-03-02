import asyncio

import streamlit as st
from api.admin_api import admin_api
from components import render_stats


async def show():
    st.title('Home')

    with st.spinner('Loading data...', show_time=True):
        try:
            rounds_count_response, rounds_count_status_code = await admin_api.get_rounds_count()
            images_count_response, images_count_status_code = await admin_api.get_images_count()
            last_rounds_response, last_rounds_status_code = await admin_api.get_last_n_rounds(10)

            if rounds_count_status_code != 200:
                st.error('Error retrieving rounds count.')
            elif images_count_status_code != 200:
                st.error('Error retrieving images count.')
            elif last_rounds_status_code != 200:
                st.error('Error retrieving latest rounds.')
            elif not rounds_count_response.get('rounds_count', None) or not last_rounds_response.get('rounds', None):
                st.success('No rounds found.')
            else:
                total_rounds = rounds_count_response['rounds_count']
                total_images = images_count_response['images_count']
                last_rounds = last_rounds_response['rounds']

                render_stats.execute(total_rounds, total_images, last_rounds)
        except Exception as e:
            st.error(f'Error retrieving rounds count: {str(e)}')


asyncio.run(show())
