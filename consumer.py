import ast
import time
import streamlit as st
from datetime import datetime
import time
from PIL import Image
import threading
import streamlit as st
import time
import queue
import datetime
from kafka import KafkaConsumer


# dashboard title
st.title("Streamlit Learning")

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


TOPIC = 'my-topic1'
consumer = KafkaConsumer(TOPIC)


# print(consumer)
def recive():
    for m in consumer:
        # print((m[6].decode("utf-8")))
        cur = (m[6].decode("utf-8"))
        res = ast.literal_eval(cur)
        # print(res['USD'])
        # print(res['GBP'])
        # print(res['EUR'])
        yield res['USD'], res['GBP'], res['EUR']


def update_dashboard():
    while True:
        time.sleep(1)
        usd = next(recive())[0]
        usd_time = datetime.datetime.now()
        print(usd_time)
        gbp = next(recive())[1]
        gbp_time = datetime.datetime.now()
        print(gbp_time)

        eur = next(recive())[2]
        eur_time = datetime.datetime.now()
        print(eur_time)

        print(usd, gbp, eur)
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Current Value", value=usd)
        col2.metric(label="Multiply by 10 ", value=gbp)
        col3.metric(label="Multiply by 10 ", value=eur)




with st.empty():
    update_dashboard()
