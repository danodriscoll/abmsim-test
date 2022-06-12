# Studio: ABMSIM-TEST
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Must be called first.
st.set_page_config(
    layout="wide", # 'centered' or 'wide'
    page_title='ABMSIM-TEST',
    menu_items={
        'About': "This is a shareable data application. Visit https://www.transmissionvamp.com."
    }
)

header = st.container()
dataset = st.container()
model = st.container()
footer = st.container()

with header:
    st.title('Agent-Based Model Simple: Test Ouput')

    with st.expander("Beginning of a System"):
        st.subheader("There shall run one coinage throughout the realm")
        st.write("A government monetary system is engineered. Money is specified in a unit of account. Law will allow (and demand) local credit relationships be settled in the government unit of account. This is a model of a hypothetical economy in which there is no private (commercial bank) money and hence there are no interest payments. In this strongly simplified economy, agents, beyond the institution of government, can be divided conceptually into their business activities on the one hand, selling services and paying out wages and, on the other hand, receiving income, consuming and accumulating assets (monetary wealth) when they act as households. The government wishes to provision itself. It buys services and pays for them with money. Money is made acceptable as a means of payment because:")

        st.markdown(
            """
            1. There is a law which makes it legal tender.
            2. Government levies taxes and ordains that these be paid in government money.
            """)

        st.write("This model describes an economy with government (high-powered) vertical money interactions and no portfolio choice. Production responds immediately to demand in this pure labour economy. The supply of labour never constitutes a constraint on production. The economy is not supply constrained; it is demand led. Whatever is demanded is produced.")
        st.write("ABMSIM analysis is limited to vertical monetary interactions between one government agent and a given number of producer household agents and consumer household agents. Consumer household agents seek employment.")

        st.subheader("Stimulus Distribution & Employment")

        st.write("At every model step, each producer agent will receive an equal share of government stimulus. Consumer agents are 'born' unemployed. Each producer will subsequently employ (by random choice) one of the consumer agents. A producer agent will check to see if the consumer agent is currently unemployed (has not been previously employed by another producer agent), else the random selection is repeated.")

        st.subheader("Simple Behaviours: Consumer Agent Rating of Government")

        st.write("Consumer agents rate the Government agent. A consumer agent will record an 'approval' rating (of Government) if it has achieved a new wealth (cash equity) 'high' at the end of the current model step. A consumer agent that has not achieved a new wealth 'high' at the end of an model step will record 'ambivalence' if it discovers, on communicating with another consumer agent (by random choice), its wealth is greater than that of the other consumer agent. 'Disapproval' is recorded when a consumer agent does not achieve a new wealth 'high' and on communicating with another consumer agent, discovers that its own wealth is either less than or equal to that of the other consumer agent.")


    with st.expander("Model Experiments"):
        st.subheader("Experiment 1")
        st.markdown(
            """
            1. Government agent stimulus: 20 Money units.
            2. Government agent tax rate: 20%.
            3. Consumption function:
                1. Proportion of disposable income: 60%.
                2. Proportion of (agent wealth) at the opening of the period (model step): 40%.
            4. Renewable energy sources compound growth: 2%.
            """)

        st.subheader("Experiment 2")
        st.write("Government tax rate: 0%; government purchasing (money stimulus): 20 monetary units. At this tax rate, ABMSIM will never reach steady state.")

        st.subheader("Experiment 3")
        st.write("Government agent tax rate: 100%; government purchasing (money stimulus): 20 monetary units. At this tax rate, both national income and government money supply remain in balance at 20 monetary units for every model step. All money supplied at the beginning of each model step is removed (returned) in total to government through taxation. Consumer agent(s), though employed, experience no disposable income and therefore enjoy no consumption.")

        st.subheader("Experiment 4")
        st.write("Government agent tax rate: 20%; government purchasing (money stimulus): 20 monetary units. At model step 85, increase the flow of government stimulus (purchasing) from 20 monetary units to 25 monetary units for each remaining model step. Disposable income, consumption and therefore national income gradually reflect the increase in government money stimulus.")

        st.subheader("Experiment 5")
        st.write("Government agent tax rate: 20%; government purchasing (money stimulus): 20 monetary units. At model step 85, decrease the flow of government stimulus (purchasing) from 20 monetary units to 15 monetary units for each remaining model step. Disposable income, consumption and therefore national income gradually reflect the decrease in government money stimulus.")

        st.subheader("Experiment 6")
        st.write("Government agent tax rate: 37%; government purchasing (adjusting money stimulus): Starting at 20 monetary units. The government agent will decide the stimulus amount for each model step based on the disapproval ratings it is receiving from consumer agents. Once 'disapproval' reaches a minimum 50% of the consumer agent population, government stimulus is increased by an amount that is between 3% and 8% (randomly decided) of the previous model step stimulus. Disposable income, consumption, national income, government fiscal balance (deficit / surplus) and of course consumer approval ratings all reflect increased government stimulus spending.")
        st.write("Experiment 6 circumvents long-run government fiscal balance exponential dynamics because:")

        st.markdown(
            """
            1. There is some level of taxation (37%).
            2. Consumer agents pay tax.
            3. Money supply is free of interest (There is no other option in ABMSIM).
            """)


    col1, col2 = st.columns(2)

    with col1:
        option = st.selectbox(
            'Select Experiment:',
            ('Experiment 1', 'Experiment 2', 'Experiment 3', 'Experiment 4', 'Experiment 5', 'Experiment 6'))

    with col2:
        st.write("Output")
        st.text("Hover over each chart for options. 'View fullscreen' and unselect / select legend categories.")        

with dataset:
    data_url = ('https://danodriscoll.github.io/abmsim-test/')

    if option == "Experiment 1":
        supply_url = data_url + "ModelSIM-Supply-Exp-1.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-1.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-1.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-1.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-1.json"
    elif option == "Experiment 2":
        supply_url = data_url + "ModelSIM-Supply-Exp-2.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-2.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-2.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-2.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-2.json"
    elif option == "Experiment 3":
        supply_url = data_url + "ModelSIM-Supply-Exp-3.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-3.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-3.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-3.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-3.json"
    elif option == "Experiment 4":
        supply_url = data_url + "ModelSIM-Supply-Exp-4.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-4.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-4.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-4.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-4.json"
    elif option == "Experiment 5":
        supply_url = data_url + "ModelSIM-Supply-Exp-5.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-5.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-5.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-5.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-5.json"
    elif option == "Experiment 6":
        supply_url = data_url + "ModelSIM-Supply-Exp-6.json"
        velocity_url = data_url + "ModelSIM-Supply-Velocity-Exp-6.json"
        approval_url = data_url + "ModelSIM-Consumer-Approval-Exp-6.json"
        wealth_url = data_url + "ModelSIM-Consumer-Agent-Wealth-Exp-6.json"
        energy_url = data_url + "ModelSIM-Macro-Energy-Flow-Demand-Exp-6.json"

    @st.cache
    def load_supply_data():
        supply_data = pd.read_json(supply_url)
        return supply_data
    def load_velocity_data():
        velocity_data = pd.read_json(velocity_url)
        return velocity_data
    def load_approval_data():
        approval_data = pd.read_json(approval_url)
        return approval_data
    def load_wealth_data():
        wealth_data = pd.read_json(wealth_url)
        return wealth_data
    def load_energy_data():
        energy_data = pd.read_json(energy_url)
        return energy_data

with model:

    # Load data.
    df_supply = load_supply_data()
    df_velocity = load_velocity_data()
    df_approval = load_approval_data()
    df_wealth = load_wealth_data()
    df_energy = load_energy_data()

    # Supply Plot
    goFig = go.Figure()
    goFig.add_trace(go.Scatter(x=df_supply['x'][0], y=df_supply['y'][0], mode=df_supply['mode'][0], name=df_supply['name'][0]))
    goFig.add_trace(go.Scatter(x=df_supply['x'][1], y=df_supply['y'][1], mode=df_supply['mode'][1], name=df_supply['name'][1]))
    goFig.add_trace(go.Scatter(x=df_supply['x'][2], y=df_supply['y'][2], mode=df_supply['mode'][2], name=df_supply['name'][2]))
    goFig.add_trace(go.Scatter(x=df_supply['x'][3], y=df_supply['y'][3], mode=df_supply['mode'][3], name=df_supply['name'][3]))                    
    goFig.add_trace(go.Scatter(x=df_supply['x'][4], y=df_supply['y'][4], mode=df_supply['mode'][4], name=df_supply['name'][4]))

    goFig.update_layout(
        margin=dict(l=50,r=50,b=50,t=50),
        template="gridon",
        xaxis_title="Model Steps",
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Monetary Units',
            titlefont_size=16,
            tickfont_size=14,
        ),        
        showlegend=True,
        legend_title="Macro Indicators",
        title=go.layout.Title(
            text="Macro Aggregates, Money Supply & Fiscal Balance: " + option,
            xref="paper",
            xanchor="center",
            yanchor="top"
        ),
        height=600
    )

    st.plotly_chart(goFig, use_container_width=True, sharing='streamlit')


    col3, col4 = st.columns(2)

    with col3:
        # Velocity Plot
        goFig1 = go.Figure()
        goFig1.add_trace(go.Scatter(x=df_velocity['x'][0], y=df_velocity['y'][0], mode=df_velocity['mode'][0], name=df_velocity['name'][0]))

        goFig1.update_layout(
            margin=dict(l=50,r=50,b=50,t=50),
            template="gridon",
            xaxis_title="Model Steps",
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Percent of GDP',
                titlefont_size=16,
                tickfont_size=14,
            ),        
            showlegend=False,
            legend_title="Macro Indicators",
            title=go.layout.Title(
                text="Change in Government Money Supply as Percent of Income (GDP): " + option,
                xref="paper",
                xanchor="center",
                yanchor="top"
            ),
            height=550
        )

        st.plotly_chart(goFig1, use_container_width=True, sharing='streamlit')

    with col4:
        # Approval Plot
        goFig2 = go.Figure()
        goFig2.add_trace(go.Scatter(x=df_approval['x'][0], y=df_approval['y'][0], mode=df_approval['mode'][0], name=df_approval['name'][0]))
        goFig2.add_trace(go.Scatter(x=df_approval['x'][1], y=df_approval['y'][1], mode=df_approval['mode'][1], name=df_approval['name'][1]))
        goFig2.add_trace(go.Scatter(x=df_approval['x'][2], y=df_approval['y'][2], mode=df_approval['mode'][2], name=df_approval['name'][2]))

        goFig2.update_layout(
            margin=dict(l=50,r=50,b=50,t=50),
            template="gridon",
            xaxis_title="Model Steps",
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Rating by Consumer Agents (Percent)',
                titlefont_size=16,
                tickfont_size=14,
            ),        
            showlegend=True,
            legend_title="Consumer Agents",
            title=go.layout.Title(
                text="Government Agent Popularity: " + option,
                xref="paper",
                xanchor="center",
                yanchor="top"
            ),
            height=550
        )

        st.plotly_chart(goFig2, use_container_width=True, sharing='streamlit')

    # Consumer Agent Wealth Plot
    goFig3 = go.Figure()
    values = list(df_wealth['y'][0])
    goFig3.add_trace(go.Bar(x=df_wealth['x'][0], y=df_wealth['y'][0],
        marker=dict(
            color=values,
            colorscale="Rdbu", 
        )    
    ))

    goFig3.update_layout(
        margin=dict(l=50,r=50,b=50,t=50),
        template="gridon",
        xaxis_title="Consumer Agent ID",
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Money Equity',
            titlefont_size=16,
            tickfont_size=14,
        ),        
        showlegend=False,
        legend_title="Model Agents",
        title=go.layout.Title(
            text="Consumer Agents Wealth: " + option,
            xref="paper",
            xanchor="center",
            yanchor="top"
        ),
        height=600
    )

    st.plotly_chart(goFig3, use_container_width=True, sharing='streamlit')

    st.markdown("---")

    # Energy Demand Flows Plot
    with st.expander("Simplistic Producer Agents Energy Demand"):
        st.write("This is a [simplistic](https://gist.github.com/danodriscoll/4c706422ac95b5b31f41c580a1848842) representation of the energy demand flows required by producer agent(s). There is an amount of fossil hydrocarbon 'energy' available. This is 'stock' energy. Renewable energy sources are available and will grow in availability compounding at a given percentage each model step. This is 'flow' energy. Each one monetary unit of combined government agent and consumer agents desires will require one unit of energy to fulfil.")
        st.write("The model uses all available 'flow' (renewable) energy with any shortfall coming from 'stock' (fossil hydrocarbon) energy. Negative externality (pollution) from 'stock' energy use is returned (to the environment agent) at 2% of total amount used.")

    goFig4 = go.Figure()
    goFig4.add_trace(go.Scatter(x=df_energy['x'][0], y=df_energy['y'][0], mode=df_energy['mode'][0], name=df_energy['name'][0]))
    goFig4.add_trace(go.Scatter(x=df_energy['x'][1], y=df_energy['y'][1], mode=df_energy['mode'][1], name=df_energy['name'][1]))
    goFig4.add_trace(go.Scatter(x=df_energy['x'][2], y=df_energy['y'][2], mode=df_energy['mode'][2], name=df_energy['name'][2]))

    goFig4.update_layout(
        margin=dict(l=50,r=50,b=50,t=50),
        template="gridon",
        xaxis_title="Model Steps",
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Energy Units',
            titlefont_size=16,
            tickfont_size=14,
        ),        
        showlegend=True,
        legend_title="Energy",
        title=go.layout.Title(
            text="Energy Demand Flows & Polution Returned to Environment: " + option,
            xref="paper",
            xanchor="center",
            yanchor="top"
        ),
        height=600
    )

    st.plotly_chart(goFig4, use_container_width=True, sharing='streamlit')

with footer:
    st.caption("View a list of [data apps](https://share.streamlit.io/danodriscoll/transvamp-apps/main/app.py). Visit the [TransmissionVamp](https://www.transmissionvamp.com) website.")
