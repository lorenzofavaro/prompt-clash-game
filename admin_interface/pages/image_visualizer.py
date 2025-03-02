import asyncio

import streamlit as st
from api.admin_api import admin_api
from components import render_images


async def show():
    st.title('Images')

    with st.spinner('Loading images...', show_time=True):
        response, status_code = await admin_api.latest_round_image_per_user()
        if status_code != 200:
            st.warning(
                f'Error loading images: status code {status_code}'
            )
            return

        render_images.execute(response)


asyncio.run(show())
