import streamlit as st


async def execute(start_func, pause_func, stop_func):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('▶️ Start', type='primary', use_container_width=True):
            try:
                response, status_code = await start_func()
                message = response.get('message')
                if status_code == 200:
                    st.balloons()
                    st.success(message)
                else:
                    st.warning(message)
            except Exception as e:
                st.error(f'Error starting the round: {str(e)}')

    with col2:
        if st.button('⏸️ Pause', type='secondary', use_container_width=True):
            try:
                response, status_code = await pause_func()
                message = response.get('message')
                if status_code == 200:
                    st.success(message)
                else:
                    st.warning(message)
            except Exception as e:
                st.error(f'Error pausing the round: {str(e)}')

    with col3:
        if st.button('⏹️ Stop', type='secondary', use_container_width=True):
            try:
                response, status_code = await stop_func()
                message = response.get('message')
                if status_code == 200:
                    st.success(message)
                else:
                    st.warning(message)
            except Exception as e:
                st.error(f'Error stopping the round: {str(e)}')
