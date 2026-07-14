import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("mobile_price_model.pkl", "rb"))

st.title("📱 Mobile Price Prediction")

battery_power = st.number_input("Battery Power")
blue = st.selectbox("Bluetooth", [0, 1])
clock_speed = st.number_input("Clock Speed")
dual_sim = st.selectbox("Dual SIM", [0, 1])
fc = st.number_input("Front Camera (MP)")
four_g = st.selectbox("4G", [0, 1])
int_memory = st.number_input("Internal Memory (GB)")
m_dep = st.number_input("Mobile Depth")
mobile_wt = st.number_input("Mobile Weight")
n_cores = st.number_input("Number of Cores")
pc = st.number_input("Primary Camera (MP)")
px_height = st.number_input("Pixel Height")
px_width = st.number_input("Pixel Width")
ram = st.number_input("RAM (MB)")
sc_h = st.number_input("Screen Height")
sc_w = st.number_input("Screen Width")
talk_time = st.number_input("Talk Time")
three_g = st.selectbox("3G", [0, 1])
touch_screen = st.selectbox("Touch Screen", [0, 1])
wifi = st.selectbox("WiFi", [0, 1])

if st.button("Predict Price Range"):
    data = pd.DataFrame([[battery_power, blue, clock_speed, dual_sim, fc,
                          four_g, int_memory, m_dep, mobile_wt,
                          n_cores, pc, px_height, px_width, ram,
                          sc_h, sc_w, talk_time, three_g,
                          touch_screen, wifi]],
                        columns=['battery_power','blue','clock_speed','dual_sim','fc',
                                 'four_g','int_memory','m_dep','mobile_wt',
                                 'n_cores','pc','px_height','px_width','ram',
                                 'sc_h','sc_w','talk_time','three_g',
                                 'touch_screen','wifi'])

    prediction = model.predict(data)

    if prediction[0] == 0:
        st.success("Price Range: Low")
    elif prediction[0] == 1:
        st.success("Price Range: Medium")
    elif prediction[0] == 2:
        st.success("Price Range: High")
    else:
        st.success("Price Range: Very High")
        