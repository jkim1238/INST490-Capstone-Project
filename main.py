import streamlit as st
import plotly.express as px
import pandas as pd


def main():
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

    # Set title.
    st.title('Total Energy Consumption Estimates by End-Use Sector')

    # Year slider.
    year = st.slider(label='Select Year:',
                     min_value=1960,
                     max_value=2019)

    # Create figure.
    fig = px.choropleth(data_frame=df,
                        locations='State',
                        locationmode='USA-states',
                        color=year,
                        scope='usa')

    # Print choropleth map figure to page.
    st.write(fig)

    # Print DataFrame.
    st.write(df)


if __name__ == '__main__':
    main()
