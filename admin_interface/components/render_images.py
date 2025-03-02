from datetime import datetime

import streamlit as st


def execute(response):
    if not response or not isinstance(response, list):
        st.success('No images generated in the last round.')
    else:
        cols = st.columns(2)
        for idx, image_data in enumerate(response):
            col = cols[idx % 2]
            with col:
                with st.container():
                    created_at = datetime.fromisoformat(
                        image_data['createdAt'].replace('Z', '+00:00')
                    ).strftime('%d-%m-%Y %H:%M:%S')

                    st.image(image_data['url'], use_container_width=True)
                    st.caption(
                        f"User: **{image_data['identifier']}**<br>Creation date: **{created_at}**",
                        unsafe_allow_html=True,
                    )
