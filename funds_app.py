import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


def analyse (params):
    result = ['**' + str(k) + '** : ' + str(v) for k,v in params.items()]
    return result

if __name__ == '__main__':
    st.image('41145630595_b3801bab65_b.jpg', use_column_width = True)
    st.title('Your Mutual Fund Advisor')
    
    st.sidebar.image('Hamla.jpg', use_column_width = True)
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

    st.sidebar.subheader('Words to Include :')
    include_words = st.sidebar.text_input('Enter words to include in search, separated by comma')
    
    st.sidebar.subheader('Words to Exclude :')
    exclude_words = st.sidebar.text_input('Enter words to exclude in search, separated by comma')
    
    params = {'look_period': look_period, 
            'fund_types': fund_types, 
            'direct_transaction': direct_transaction,
            'regular_transaction': regular_transaction,
            'mf_type': mf_type,
            'performance_priority': performance_priority,
            'include_words': include_words.split(','),
            'exclude_words': exclude_words.split(',')
            }

    results = analyse(params)

    for k in results:
        st.markdown(k)
    st.subheader('The result of any function, using above as parameters, may be displayed here.')

