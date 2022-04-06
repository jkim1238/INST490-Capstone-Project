import streamlit as st
import plotly.express as px
import pandas as pd


def main():
    # Set page config.
    st.set_page_config(page_title='INST 490 Capstone Project',
                       page_icon='💡',
                       initial_sidebar_state='expanded')

    # Print title.
    st.title('INST 490 Capstone Project')

    # Print team member names.
    st.write('Mohamed Nabeel, Grant Buttrey, Jiin Kim, Mahad Abdi, Matthew Makonnen, Fabrice Tedonjeu')

    # Set header.
    st.header('Total Energy Consumption Estimates by End-Use Sector')

    # Read total energy consumption data.
    df = pd.read_excel(io=r'use_tot_sector.xlsx',
                       sheet_name='Total Consumption',
                       header=2)

    # Drop first row.
    df.drop(index=df.index[0],
            axis=0,
            inplace=True)

    # Drop last row.
    df.drop(index=df.index[-1],
            axis=0,
            inplace=True)

    # Year slider.
    year = st.slider(label='Select Year:',
                     min_value=1960,
                     max_value=2019)

    # Create figure.
    fig = px.choropleth(data_frame=df,
                        locations='State',
                        locationmode='USA-states',
                        color=year,
                        scope='usa',
                        title=f'Total Energy Consumption Estimates U.S. {year}',
                        labels={f'{year}': 'Billion Btu'})

    # Print choropleth map figure to page.
    st.write(fig)

    # Set header for raw data.
    st.header('Raw Data')

    # Print DataFrame.
    st.write(df)


if __name__ == '__main__':
    main()
