import streamlit as st
import streamlit_authenticator as stauth
from components import render_login
from components import render_sidebar
from config import config
from utils.logger import logger


def route_login(admin_pages, authenticator):
    if st.session_state['authentication_status']:
        logger.debug(
            f"User successfully authenticated: {st.session_state.get('username')}"
        )
        render_sidebar.execute(authenticator, admin_pages)
        pg = st.navigation(admin_pages)
        pg.run()
    elif st.session_state['authentication_status'] is False:
        logger.warning(f'Failed login attempt')
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')


if __name__ == '__main__':
    st.set_page_config(
        page_title='Admin Panel',
        layout='wide',
        page_icon='🛠️'
    )
    st.markdown("""<style>.stAppToolbar {display: none;}</style>""", unsafe_allow_html=True)
    st.logo(
        'res/logo.png',
        size='large',
        icon_image='res/logo.png',
    )

    authenticator = stauth.Authenticate(
        config.credentials,
        config.cookie['name'],
        config.cookie['key'],
        config.cookie['expiry_days'],
    )

    home_page = st.Page('pages/home.py', title='Home', icon='🏠')
    image_visualizer_page = st.Page(
        'pages/image_visualizer.py', title='Images', icon='🖼️'
    )
    round_controller_page = st.Page(
        'pages/round_controller.py', title='Round Control', icon='🔄'
    )
    admin_pages = [home_page, round_controller_page, image_visualizer_page]

    render_login.execute(authenticator)
    route_login(admin_pages, authenticator)
