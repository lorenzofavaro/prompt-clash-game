import streamlit as st


def execute(authenticator):
    try:
        authenticator.login()
    except Exception as e:
        st.error(e)
