import asyncio

import streamlit as st
from api.admin_api import admin_api
from components import render_control_buttons
from components import render_settings_selector


async def show():
    st.title('Round Controller')

    # Settings selector
    await render_settings_selector.execute(admin_api.get_all_themes, admin_api.save_settings)

    st.markdown('---')

    # Control buttons
    await render_control_buttons.execute(
        admin_api.start_round, admin_api.pause_round, admin_api.stop_round
    )


asyncio.run(show())
