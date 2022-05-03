import streamlit as st
import plotly.express as px
import pandas as pd


def main():
    # Set page config.
    st.set_page_config(page_title='DMV Energy Efficiency Analysis',
                       page_icon='💡',
                       initial_sidebar_state='expanded')

    # Print title.
    st.title(body='💡 DMV Energy Efficiency Analysis',
             anchor='title')

    # Print team member names.
    st.write('Mohamed Nabeel, Grant Buttrey, Jiin Kim, Mahad Abdi, Matthew Makonnen, Fabrice Tedonjeu')

    # Summary header.
    st.header(body='Summary')

    # The summary.
    st.write("""
             The DMV Energy Efficiency Analysis details the current energy status of the DMV region, in regards to 
             energy consumption and cost, while also providing programs and policies states within the region can implement to 
             improve energy efficiency.
             """)

    # Choose dataset header.
    st.header(body='Choose Dataset',
              anchor='choose-dataset')

    # Select box to choose dataset.
    visualization = st.selectbox(label='Select a dataset:',
                                 options=('Energy Consumption', 'Energy Usage Price'))

    # Table of contents.
    st.sidebar.title(body='Table of Contents')

    # The contents.
    contents = """
               - [Summary](#summary)\n
               - [Choose Dataset](#choose-dataset)\n
               - [Data Visualization](#data-visualization)\n
                   - [Choropleth Map](#choropleth-map)\n
                   - [Line Plot](#line-plot)\n
               - [Machine Learning](#machine-learning)\n
                   - [Scatter Plot with Linear Regression Model](#scatter-plot)\n
                   - [Equation](#equation)\n
                   - [Prediction](#prediction)\n
               - [Data Analysis](#data-analysis)\n
               - [Recommendations](#recommendations)
               """

    # Place table of contents in sidebar.
    st.sidebar.markdown(body=contents,
                        unsafe_allow_html=True)

    # Sidebar return to top link.
    st.sidebar.markdown(body='<a href="#title">Link to top</a>',
                        unsafe_allow_html=True)

    # Header for Data Visualization.
    st.header(body='Data Visualization')

    if visualization == 'Energy Consumption':
        # Set subheader.
        st.subheader(body='Total Energy Consumption Estimates by End-Use Sector, 1990-2019')

        # Write description.
        st.write('Comprehensive state-level estimates of energy production, consumption, prices, and expenditures by '
                 'source and sector.')

        # Subheader for choropleth map.
        st.subheader(body='Choropleth Map')

        # Subheader for U.S.
        st.markdown(body='#### United States')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector1')
        with col2:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1960,
                             max_value=2019,
                             key='slider1')

        # Get dataframe.
        df = get_choro_us_usage_df(sector)

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

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption U.S. {sector} {year} Data')
        file_container.write(df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv1')

        # Subheader for DMV.
        st.markdown(body='#### DMV')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector2')
        with col2:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1960,
                             max_value=2019,
                             key='slider2')

        # Get dataframe.
        dmv_df = get_choro_dmv_usage_df(sector)

        # Create choropleth map figure.
        fig = px.choropleth(data_frame=dmv_df,
                            locations='State',
                            locationmode='USA-states',
                            color=year,
                            scope='usa',
                            title=f'Total Energy Consumption Estimates DMV {sector} {year}',
                            labels={f'{year}': 'Billion Btu'})

        fig.update_geos(fitbounds='locations')

        # Print choropleth map figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption DMV {sector} {year} Data')
        file_container.write(df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv2')

        # Subheader for line plot.
        st.subheader(body='Line Plot',
                     anchor='line-plot')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector3')
        with col2:
            # Slider for year range.
            years = st.slider(label='Select a year range:',
                              min_value=1960,
                              max_value=2019,
                              value=(1960, 2019),
                              key='range1')

        # Get dataframe.
        line_df = get_line_usage_df(sector, years)

        # Create line plot figure.
        fig = px.line(data_frame=line_df,
                      x='Year',
                      y='value',
                      color='State',
                      title=f'Total Energy Consumption Estimates DMV {sector} {years[0]}-{years[1]}',
                      labels={'value': 'Energy Consumption (Billion Btu)'})

        # Print line plot figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption DMV {sector} '
                                           f'{years[0]}-{years[1]} Data')
        file_container.write(line_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=line_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv3')

        # Header for machine learning.
        st.header(body='Machine Learning',
                  anchor='machine-learning')

        # Description for machine learning.
        st.write('Because we don\'t have data for recent years, we can use machine learning to predict values for any '
                 'year.')

        # Subheader for linear regression model.
        st.subheader(body='Scatter Plot with Linear Regression Model',
                     anchor='scatter-plot')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose state.
            state = st.selectbox(label='Select a state:',
                                 options=('US', 'DC', 'MD', 'VA'))

        with col2:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector4')

        # Get dataframe.
        scatter_df = get_scatter_usage_df(sector, state)

        # Create scatter plot figure.
        fig = px.scatter(data_frame=scatter_df,
                         x='Year',
                         y='value',
                         color='State',
                         title=f'Total Energy Consumption Estimates {state} {sector} 1960-2019',
                         labels={'value': 'Energy Consumption (Billion Btu)'},
                         trendline='ols',
                         trendline_color_override='red')

        # Print scatter plot figure to page.
        st.write(fig)

        # Get OLS results.
        results = px.get_trendline_results(fig)

        # Print summary.
        file_container = st.expander(label='Click to display Model Parameters')
        file_container.write(results.px_fit_results.iloc[0].summary())

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption {state} {sector} '
                                           f'1960-2019 Data')
        file_container.write(scatter_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv4')

        # Get coefficients.
        b = results.iloc[0]['px_fit_results'].params[0]
        m = results.iloc[0]['px_fit_results'].params[1]

        # Print subheader.
        st.subheader(body='Equation')

        # Print equation.
        st.write('Total Energy Consumption Estimates ', state, ' ', sector, ' 1960-2019')
        st.latex(f'y = {m}x + {b}')

        # Print subheader for prediction.
        st.subheader(body='Prediction',
                     anchor='prediction')

        year = st.number_input(label='Enter a year:',
                               value=2022,
                               format='%d')

        # Print explanation.
        st.write('Using Ordinary Least Squares (OLS) linear regression model, we predict that the Total Energy '
                 'Consumption Estimates ', state, ' ', sector, ' will consume ', calculate_prediction(m, year, b),
                 ' billion Btu of energy in ', year, '.')
    elif visualization == 'Energy Usage Price':
        # Set subheader.
        st.subheader(body='Average Price by State by Provider, 1990-2020')

        # Write description.
        st.write('Revenue, sales, customer counts, and retail price by state and sector.')

        # Subheader for choropleth map.
        st.subheader(body='Choropleth Map')

        # Subheader for U.S.
        st.markdown(body='#### United States')

        # Set 3 columns for the options.
        col1, col2, col3 = st.columns(3)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total', 'Residential', 'Commercial', 'Industrial', 'Transportation',
                                           'Other'),
                                  key='sector1')

        with col2:
            # Select box to choose provider.
            provider = st.selectbox(label='Select a provider:',
                                    options=('Total Electric Industry', 'Full-Service Providers',
                                             'Restructured Retail Service Providers', 'Energy-Only Providers',
                                             'Delivery-Only Providers'),
                                    key='provider1')

        with col3:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1990,
                             max_value=2020,
                             key='slider1')

        # Get dataframe.
        df = get_choro_us_price_df(sector, provider, year)

        # Create figure.
        fig = px.choropleth(data_frame=df,
                            locations='State',
                            locationmode='USA-states',
                            color=sector,
                            scope='usa',
                            title=f'Average Price U.S. {sector} Sector {provider} {year}',
                            labels={f'{sector}': 'cents/kWh'},
                            color_continuous_scale='Blues')

        # Print choropleth map figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Average Price U.S. {sector} Sector {provider} {year} '
                                           f'Data')
        file_container.write(df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv1')

        # Subheader for DMV.
        st.markdown(body='#### DMV')

        # Set 3 columns for the options.
        col1, col2, col3 = st.columns(3)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total', 'Residential', 'Commercial', 'Industrial', 'Transportation',
                                           'Other'),
                                  key='sector2')

        with col2:
            # Select box to choose provider.
            provider = st.selectbox(label='Select a provider:',
                                    options=('Total Electric Industry', 'Full-Service Providers',
                                             'Restructured Retail Service Providers', 'Energy-Only Providers',
                                             'Delivery-Only Providers'),
                                    key='provider2')

        with col3:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1990,
                             max_value=2020,
                             key='slider2')

        # Get dataframe.
        dmv_df = get_choro_dmv_price_df(sector, provider, year)

        # Create choropleth map figure.
        fig = px.choropleth(data_frame=dmv_df,
                            locations='State',
                            locationmode='USA-states',
                            color=sector,
                            scope='usa',
                            title=f'Average Price DMV {sector} Sector {provider} {year}',
                            labels={f'{sector}': 'cents/kWh'},
                            color_continuous_scale='Blues')

        fig.update_geos(fitbounds='locations')

        # Print choropleth map figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Average Price DMV {sector} Sector {provider} {year} '
                                           f'Data')
        file_container.write(dmv_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv2')

        # Subheader for line plot.
        st.subheader('Line Plot',
                     anchor='line-plot')

        # Set 3 columns for the options.
        col1, col2, col3 = st.columns(3)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total', 'Residential', 'Commercial', 'Industrial', 'Transportation',
                                           'Other'),
                                  key='sector3')

        with col2:
            # Select box to choose provider.
            provider = st.selectbox(label='Select a provider:',
                                    options=('Total Electric Industry', 'Full-Service Providers',
                                             'Restructured Retail Service Providers', 'Energy-Only Providers',
                                             'Delivery-Only Providers'),
                                    key='provider3')
        with col3:
            # Slider for year range.
            years = st.slider(label='Select a year range:',
                              min_value=1990,
                              max_value=2020,
                              value=(1990, 2020),
                              key='range1')

        # Get dataframe.
        dmv_df = get_line_price_df(sector, provider, years)

        # Create line plot figure.
        fig = px.line(data_frame=dmv_df,
                      x='Year',
                      y=sector,
                      color='State',
                      title=f'Average Price DMV {sector} Sector {provider} {years[0]}-{years[1]}',
                      labels={'Total': 'Average Price (Cents/kWh)'})

        # Print line plot figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Average Price DMV {sector} Sector {provider} {years[0]}-'
                                           f'{years[1]} Data')
        file_container.write(dmv_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv3')

        # Header for machine learning.
        st.header(body='Machine Learning',
                  anchor='machine-learning')

        # Description for machine learning.
        st.write('Because we don\'t have data for recent years, we can use machine learning to predict values for any '
                 'year.')

        # Subheader for linear regression model.
        st.subheader(body='Scatter Plot with Linear Regression Model',
                     anchor='scatter-plot')

        # Set 3 columns for the options.
        col1, col2, col3 = st.columns(3)

        with col1:
            # Select box to choose state.
            state = st.selectbox(label='Select a state:',
                                 options=('US', 'DC', 'MD', 'VA'))

        with col2:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total', 'Residential', 'Commercial', 'Industrial', 'Transportation',
                                           'Other'),
                                  key='sector4')

        with col3:
            # Select box to choose provider.
            provider = st.selectbox(label='Select a provider:',
                                    options=('Total Electric Industry', 'Full-Service Providers',
                                             'Restructured Retail Service Providers', 'Energy-Only Providers',
                                             'Delivery-Only Providers'),
                                    key='provider4')

        # Get dataframe.
        scatter_df = get_scatter_price_df(sector, provider, state)

        # Create scatter plot figure.
        fig = px.scatter(data_frame=scatter_df,
                         x='Year',
                         y=sector,
                         color='State',
                         title=f'Average Price {state} {sector} Sector {provider} 1990-2020',
                         labels={'Total': 'Average Price (Cents/kWh)'},
                         trendline='ols',
                         trendline_color_override='red')

        # Print scatter plot figure to page.
        st.write(fig)

        # Get OLS results.
        results = px.get_trendline_results(fig)

        # Print summary.
        file_container = st.expander(label='Click to display Model Parameters')
        file_container.write(results.px_fit_results.iloc[0].summary())

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Average Price {state} {sector} Sector {provider} 1990'
                                           f'-2020 Data')
        file_container.write(scatter_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv4')

        # Get coefficients.
        b = results.iloc[0]['px_fit_results'].params[0]
        m = results.iloc[0]['px_fit_results'].params[1]

        # Print subheader.
        st.subheader(body='Equation')

        # Print equation.
        st.write('Average Price ', state, ' ', sector, ' Sector ', provider, ' 1990-2020')
        st.latex(f'y = {m}x + {b}')

        # Print subheader for prediction.
        st.subheader(body='Prediction',
                     anchor='prediction')

        year = st.number_input(label='Enter a year:',
                               value=2022,
                               format='%d')

        # Print explanation.
        st.write('Using Ordinary Least Squares (OLS) linear regression model, we predict that the Average Price ',
                 state, ' ', sector, ' Sector ', provider, ' will cost ', calculate_prediction(m, year, b),
                 ' Cents/kWh in ', year, '.')

    # Print header for data analysis.
    st.header(body='Data Analysis',
              anchor='data-analysis')

    # Print analysis.
    st.write(""" 
    ###### MD
    - The minimum amount of energy that Maryland consumed was 142,516 billion BTU.
    - The average amount of energy that Maryland consumed was 325,176 billion BTU.
    - The maximum amount of energy that Maryland consumed was 454,757 billion BTU.
    - The average price of energy use in Maryland cost $3,625,714.
    
    ###### DC
    - The minimum amount of energy that DC consumed was 24,123 billion BTU.
    - The minimum amount of energy that DC consumed was 34,855 billion BTU.
    - The minimum amount of energy that DC consumed was 42,435 billion BTU.
    - The average price of energy use in DC cost $414,776.

    ###### VA
    - The minimum amount of energy that Virginia consumed was 192,104 billion BTU.
    - The minimum amount of energy that Virginia consumed was 449,575 billion BTU.
    - The minimum amount of energy that Virginia consumed was 683,534 billion BTU.
    - The average price of energy use in Virginia cost $7,341,56
    """)

    # Print header.
    st.markdown(body='###### Insights & Findings ')

    # Print insights.
    st.write(""" 
    Based on the data analysis, we can make the inference that the DMV region has experienced 
    an increase in energy consumption and energy usage price. This means that, with the current 
    status of energy inefficiency across the states within the DMV region, there is a need for 
    the implementation of energy efficiency policies and programs to help improve energy efficiency in the DMV.
    """)

    # Print header/subheader for Recommendations.
    st.header(body='Recommendations',
              anchor='recommendations')

    # Print markdown
    st.markdown(body='###### State-Level Energy Efficiency Programs')

    # Print DMV.
    st.write("""
    -	MD
    	- PEPCO - Commercial and Industrial Energy Efficiency Rebate Program
    	- PEPCO - Residential Energy Efficiency Rebate Program
    -	DC
        - FirstEnergy (Potomac Edison) - Commercial and Industrial Energy Efficiency Rebate Program
        - FirstEnergy (Potomac Edison) - Residential Energy Efficiency Rebate Program
    -	VA
        - Washington Gas - Commercial Energy Efficiency Rebate Program
        - Washington Gas - Residential Energy Efficiency Rebate Program 
    """)

    # Print markdown
    st.markdown(body='###### State-Level Energy Efficiency Policies')

    # Print policies.
    st.write("""
    -	Encourage retro-commissioning when it comes to developing and building public and private buildings.
    -	Implement state-wide energy performance building codes for the numerous commercial and residential buildings constructed or in the process of construction.
    -	Provide educational classes and materials that help state citizens adjust their lifestyle to be more energy conscious and follow energy-efficient methods.
    -	Implement energy efficiency standards and codes for household appliances, like washing machines and refrigerators, to encourage more energy-efficient appliances.
    -	Monitor the state's ongoing energy consumption and cost analysis to curate energy efficiency programs and policies for the state's current energy status.
    """)

    # Return to top link.
    st.markdown(body='<a href="#title">Link to top</a>',
                unsafe_allow_html=True)

    # # Remove top right menu.
    st.markdown(body="""
                     <style>
                     header {visibility: hidden;}
                     #MainMenu {visibility: hidden;}
                     footer {visibility: hidden;}
                     </style>
                     """,
                unsafe_allow_html=True)


@st.cache
def get_choro_us_usage_df(sector):
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

    return df


@st.cache
def get_choro_dmv_usage_df(sector):
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

    # Drops states except DMV.
    df = df[df['State'].isin(['DC', 'MD', 'VA'])]

    return df


@st.cache
def get_line_usage_df(sector, years):
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

    # Drops states except DMV.
    df = df[df['State'].isin(['DC', 'MD', 'VA'])]

    # Make years a column for plotting.
    df = pd.melt(frame=df,
                 id_vars=['State'],
                 var_name='Year')

    # Filter between year range.
    df = df[df['Year'] >= years[0]]
    df = df[df['Year'] <= years[1]]

    return df


@st.cache
def get_scatter_usage_df(sector, state):
    # Read total energy consumption data.
    df = pd.read_excel(io=r'use_tot_sector.xlsx',
                       sheet_name=sector,
                       header=2)

    # Drop first row.
    df.drop(index=df.index[0],
            axis=0,
            inplace=True)

    # Drop other states.
    df = df[df['State'].isin(['DC', 'MD', 'VA', 'US'])]
    df = df[df['State'] == state]

    # Make years a column for plotting.
    df = pd.melt(frame=df,
                 id_vars=['State'],
                 var_name='Year')

    return df


@st.cache
def get_choro_us_price_df(sector, provider, year):
    # Read average price data.
    df = pd.read_excel(io=r'avgprice_annual.xlsx',
                       sheet_name='Price',
                       header=1)

    # Filter sector, provider, and year.
    df = df[df['Year'] == year]
    df = df[df['Industry Sector Category'] == provider]
    df = df[['Year', 'State', 'Industry Sector Category', f'{sector}']]

    return df


@st.cache
def get_choro_dmv_price_df(sector, provider, year):
    # Read average price data.
    df = pd.read_excel(io=r'avgprice_annual.xlsx',
                       sheet_name='Price',
                       header=1)

    # Filter sector, provider, and year.
    df = df[df['Year'] == year]
    df = df[df['Industry Sector Category'] == provider]
    df = df[['Year', 'State', 'Industry Sector Category', f'{sector}']]

    # Drops states except DMV.
    df = df[df['State'].isin(['DC', 'MD', 'VA'])]

    return df


@st.cache
def get_line_price_df(sector, provider, years):
    # Read average price data.
    df = pd.read_excel(io=r'avgprice_annual.xlsx',
                       sheet_name='Price',
                       header=1)

    # Filter sector and provider.
    df = df[df['Industry Sector Category'] == provider]
    df = df[['Year', 'State', 'Industry Sector Category', f'{sector}']]

    # Drops states except DMV.
    df = df[df['State'].isin(['DC', 'MD', 'VA'])]

    # Filter between year range.
    df = df[df['Year'] >= years[0]]
    df = df[df['Year'] <= years[1]]

    return df


@st.cache
def get_scatter_price_df(sector, provider, state):
    # Read average price data.
    df = pd.read_excel(io=r'avgprice_annual.xlsx',
                       sheet_name='Price',
                       header=1)

    # Filter sector and provider.
    df = df[df['Industry Sector Category'] == provider]
    df = df[['Year', 'State', 'Industry Sector Category', f'{sector}']]

    # Drops states except DMV.
    df = df[df['State'].isin(['DC', 'MD', 'VA', 'US'])]
    df = df[df['State'] == state]

    return df


@st.cache
def calculate_prediction(m, year, b):
    return m * year + b


if __name__ == '__main__':
    main()
