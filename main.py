import streamlit as st
import plotly.express as px
import pandas as pd


def main():
    # Set page config.
    st.set_page_config(page_title='INST 490 Capstone Project',
                       page_icon='💡',
                       initial_sidebar_state='expanded')

    # Print title.
    st.title(body='💡 INST 490 Capstone Project')

    # Print team member names.
    st.write('Mohamed Nabeel, Grant Buttrey, Jiin Kim, Mahad Abdi, Matthew Makonnen, Fabrice Tedonjeu')

    # Set header.
    st.header(body='Total Energy Consumption Estimates by End-Use Sector')

    # Write description.
    st.write('Comprehensive state-level estimates of energy production, consumption, prices, and expenditures by '
             'source and sector.')

    # Select box to choose sector.
    sector = st.selectbox(label='Select a sector:',
                          options=('Total Consumption', 'Residential Sector', 'Commercial Sector', 'Industrial Sector', 'Transportation Sector'))

    # Read total energy consumption data.
    df = pd.read_excel(io=r'use_tot_sector.xlsx',
                       sheet_name=sector,
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
    year = st.slider(label='Select a year:',
                     min_value=1960,
                     max_value=2019)

    # Create figure.
    fig = px.choropleth(data_frame=df,
                        locations='State',
                        locationmode='USA-states',
                        color=year,
                        scope='usa',
                        title=f'Total Energy Consumption Estimates U.S. {sector} {year}',
                        labels={f'{year}': 'Billion Btu'})

    # Print choropleth map figure to page.
    st.write(fig)

    # Set header for raw data.
    st.header(body='Raw Data')

    # Print DataFrame.
    file_container = st.expander("Display Raw Data .xlsx")
    file_container.write(df)

    # Save raw data button to save DataFrame as CSV file.
    st.download_button(label="Press to Download Raw Data",
                       data=df.to_csv(),
                       file_name="file.csv",
                       mime="text/csv",
                       key='download-csv')


if __name__ == '__main__':
    main()
