def style_for_st():
    import streamlit as st
    st.sidebar.markdown("""
    <style>
    .metric-card {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    padding: 15px;
    border-radius: 12px;
    color: black;
    text-align: center;
    font-weight: bold;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    transition: all 0.3s ease-in-out;
    }
    .metric-card:hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 15px rgba(255,255,255,0.4);
    }
    .metric-title {
    font-size: 0.9em;
    color: #2d3436;
    }
    .metric-value {
    font-size: 1.3em;
    color: #004d40;
    }
    .divider {
    border-bottom: 2px solid #83c5be;
    margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""<style>[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #232526, #414200);
    color: white;
    }
    .title{
    color:#83c5be;
    font-weight: bold;
    text-shadow: 2px 2px 4px grey;
    }
    .stVerticalBlockBorderWrapperone{
    background: linear-gradient(to right, #232526, #414330)
    }
    <\style>""",unsafe_allow_html=True)
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
    background: linear-gradient(to left, #232526, #414330);
    color: white;
    border-right: 2px solid #83c5be;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {
    color: #83c5be !important;
    }
    </style>
    """, unsafe_allow_html=True)