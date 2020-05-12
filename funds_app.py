import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


def analyse (params):
    result = '\n'.join([str(x) for x in params.values()])
    return result

if __name__ == '__main__':
    st.title('Your Mutual Fund Advisor')
    
    st.sidebar.subheader('look Period :')
    look_period = st.sidebar.selectbox(
            'Select Any One',
                [1, 3, 6, 12],
                0,
                lambda x : f'{x} Month' if x==1 else  f'{x} Months')
    
    fund_categories = [
            "Open Fund (Debt)",
            "Open Fund (Equity)",
            "Open Fund (Debt + Equity)",
            "Open Fund (Currency)",
            "Closed Fund (Debt)",
            "Closed Fund (Equity)",
            ]
    
    st.sidebar.subheader('Fund categories :')
    fund_types = st.sidebar.multiselect(
            'Select All Applicable',
                fund_categories,
                [])
    
    st.sidebar.subheader('Transaction Mode :')
    direct_transaction = st.sidebar.checkbox('Direct')
    regular_transaction = st.sidebar.checkbox('Regular')
    
    st.sidebar.subheader('MF Type :')
    mf_type = st.sidebar.radio(
            'Select Any One',
            ('Dividend', 'Growth'))
    
    st.sidebar.subheader('Performance Priority :')
    performance_priority = st.sidebar.radio(
            'Select Any One',
            ('Alpha', 'Beta', 'Balanced'))
    
    params = {'look_period': look_period, 
            'fund_categories': fund_categories, 
            'fund_types': fund_types, 
            'direct_transaction': direct_transaction,
            'direct_transaction': direct_transaction,
            'mf_type': mf_type,
            'performance_priority': performance_priority
            }

    results = analyse(params)

    st.text_area('Display Results Here', results)

