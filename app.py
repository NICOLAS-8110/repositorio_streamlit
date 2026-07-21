import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n): # función que emula el lanzamiento de una moneda

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
No te preocupes si no comprendes totalmente la función toss_coin(), no tiene nada de malo, no es necesario que comprendas todas las funciones que utilizas. Por ejemplo, cuando llamas a la función read_csv() desde Pandas, no necesariamente sabes cómo funciona, pero aún así puedes usarla. En este caso sucede lo mismo.

Ahora, vamos a llamar a toss_coin pulsando el botón start_button (obtiene el valor True).

import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    mean = toss_coin(number_of_trials)