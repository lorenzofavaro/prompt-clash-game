import streamlit as st


async def execute(get_themes_func, save_func):
    if st.session_state.get('themes', None):
        available_themes = st.session_state['themes']
    else:
        response, status_code = await get_themes_func()

        if status_code != 200:
            st.error('Error retrieving available themes.')
            return

        if not response:
            st.warning('No themes available.')
            return

        available_themes = [''] + [item['title'] for item in response['themes']]
        st.session_state['themes'] = available_themes

    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    with col1:
        minutes = st.number_input(
            'Minutes',
            min_value=0,
            max_value=59,
            value=0,
            step=1,
        )
    with col2:
        seconds = st.number_input(
            'Seconds',
            min_value=0,
            max_value=59,
            value=0,
            step=10,
        )
    with col3:
        total_seconds = (minutes * 60) + seconds
        st.metric('Total Time', f'{minutes}m {seconds}s')

    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col1:
        selected_theme = st.selectbox(
            'Select Theme',
            options=available_themes,
            help='Choose a theme for the round',
        )

        if st.button(
            '💾 Save Settings', type='secondary', use_container_width=True
        ):
            try:
                settings = {
                    'minutes': minutes,
                    'seconds': seconds,
                    'theme': selected_theme,
                }
                _, status_code = await save_func(settings)
                if status_code == 200:
                    st.success('Settings saved successfully!')
                else:
                    st.error('Unable to save settings.')
            except Exception as e:
                st.error(f'Error saving settings: {str(e)}')
