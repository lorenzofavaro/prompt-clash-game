import pandas as pd
import streamlit as st
from utils.time_formatter import format_duration
from utils.time_formatter import format_timestamp


def format_round_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df['start_timestamp'] = df['start_timestamp'].apply(format_timestamp)
    df['end_timestamp'] = df['end_timestamp'].apply(format_timestamp)
    df['time_duration'] = df['time_duration'].apply(format_duration)
    return df


def execute(total_rounds, total_images, last_rounds):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label='Total Rounds', value=total_rounds)
        with col2:
            st.metric(label='Generated Images', value=total_images)

        st.divider()

        st.write('**Last 10 rounds**')
        df = pd.DataFrame(last_rounds)
        df = format_round_dataframe(df)

        df = df.rename(
            columns={
                'id': 'ID',
                'theme': 'Theme',
                'start_timestamp': 'Start Date',
                'end_timestamp': 'End Date',
                'time_duration': 'Duration',
            }
        )

        st.dataframe(df, hide_index=True, use_container_width=True)
