import streamlit as st
import time
import datetime

st.title('Test timeout')

st.write('This is a test to see if the app times out after 30 minutes.')
st.write('When deployed on streamlit, the app will pop up a message "Tried to use SessionInfo before it was initialized." after 30 minutes.')

txt = st.text('')


def update_ui():
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        formated_time = str(datetime.timedelta(seconds=elapsed_time))
        content = f"Elapsed Time: {formated_time}"
        txt.text(content)
        time.sleep(1)

update_ui()
