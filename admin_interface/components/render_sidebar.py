import streamlit as st


def execute(authenticator, admin_pages):
    logout = authenticator.logout(location='sidebar')
    with st.sidebar:
        for page in admin_pages:
            st.page_link(page, label=page.title, icon=page.icon)
