import streamlit as st
import scipy.stats
import time
import pandas as pd


if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_expreriment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no','iteraciones','media'])


st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toos_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)
    return mean

number_of_trials = st.slider('¿Número de intentos ?', 1 , 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso')
    st.session_state['experiment_no'] += 1
    mean = toos_coin(number_of_trials)
    nuevo_df = pd.DataFrame(data=[[st.session_state['experiment_no'],
                               number_of_trials,
                               mean]],
                        columns=['no', 'iteraciones', 'media'])

    if 'df_experiment_results' not in st.session_state or st.session_state['df_experiment_results'].empty:
        st.session_state['df_experiment_results'] = nuevo_df
      #  print("es la primera vez")
    else:
        print("ya existe")
        st.session_state['df_experiment_results'] = pd.concat([
            st.session_state['df_experiment_results'],
            nuevo_df
        ], axis=0)
        st.session_state['df_experiment_results'].reset_index(drop=True, inplace=True)
 #   print(st.session_state['df_experiment_results'])
st.write(st.session_state['df_experiment_results'])

