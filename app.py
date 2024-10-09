
# #====================first chart then show data option ===============================================

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Page configuration
# st.set_page_config(layout="wide")  # To make the layout wider for better visualizations

# # Title and Header
# st.title("Dynamic CSV Data Dashboard")
# st.header("Automated Exploratory Data Analysis")

# # Sidebar for uploading CSV
# st.sidebar.header("Upload your CSV file")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# # Function to load data
# @st.cache_data
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

# # If file is uploaded, process the data
# if uploaded_file is not None:
#     df = load_data(uploaded_file)

#     # Detect numeric columns for histograms
#     numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

#     # Detect categorical columns for bar charts
#     categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

#     # Creating columns to display 4 charts together
#     st.subheader("Key Visualizations")
    
#     col1, col2, col3, col4 = st.columns(4)
    
#     # First numeric column histogram
#     if len(numeric_columns) > 0:
#         with col1:
#             st.subheader(f"Distribution of {numeric_columns[0]}")
#             fig, ax = plt.subplots()
#             sns.histplot(df[numeric_columns[0]], kde=True, ax=ax)
#             st.pyplot(fig)

#     # Second numeric column histogram
#     if len(numeric_columns) > 1:
#         with col2:
#             st.subheader(f"Distribution of {numeric_columns[1]}")
#             fig, ax = plt.subplots()
#             sns.histplot(df[numeric_columns[1]], kde=True, ax=ax)
#             st.pyplot(fig)

#     # First categorical column bar chart
#     if len(categorical_columns) > 0:
#         with col3:
#             st.subheader(f"Distribution of {categorical_columns[0]}")
#             fig, ax = plt.subplots()
#             sns.countplot(x=categorical_columns[0], data=df, ax=ax)
#             st.pyplot(fig)

#     # Second categorical column bar chart
#     if len(categorical_columns) > 1:
#         with col4:
#             st.subheader(f"Distribution of {categorical_columns[1]}")
#             fig, ax = plt.subplots()
#             sns.countplot(x=categorical_columns[1], data=df, ax=ax)
#             st.pyplot(fig)

#     # Adding an expander to show/hide raw data
#     with st.expander("Show Raw Data"):
#         st.write("Here is the raw data you uploaded:")
#         st.write(df)

#         # Let users select specific columns to display
#         selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
#         st.write(df[selected_columns])

#     # Data Summary for numeric columns
#     if df.select_dtypes(include='number').shape[1] > 0:
#         st.subheader("Summary Statistics for Numeric Columns")
#         st.write(df.describe())

#     # Additional visualizations for any extra columns
#     st.subheader("Additional Visualizations")

#     if len(numeric_columns) > 2:
#         st.write(f"Distribution of {numeric_columns[2]}")
#         fig, ax = plt.subplots()
#         sns.histplot(df[numeric_columns[2]], kde=True, ax=ax)
#         st.pyplot(fig)

#     if len(categorical_columns) > 2:
#         st.write(f"Distribution of {categorical_columns[2]}")
#         fig, ax = plt.subplots()
#         sns.countplot(x=categorical_columns[2], data=df, ax=ax)
#         st.pyplot(fig)

# else:
#     st.write("Please upload a CSV file to see the dashboard.")



# #==================================chart comaparisoon with one column ====================

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Page configuration
# st.set_page_config(layout="wide")  # To make the layout wider for better visualizations

# # Title and Header
# st.title("Dynamic CSV Data Dashboard")
# st.header("Automated Exploratory Data Analysis")

# # Sidebar for uploading CSV
# st.sidebar.header("Upload your CSV file")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# # Function to load data
# @st.cache_data
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

# # If file is uploaded, process the data
# if uploaded_file is not None:
#     df = load_data(uploaded_file)

#     # Detect numeric columns
#     numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

#     # Ensure there is at least one numeric column for reference
#     if len(numeric_columns) > 0:
#         reference_column = numeric_columns[0]  # Use the first numeric column as the reference
        
#         # Sidebar for selecting visualization type
#         st.sidebar.header("Select Visualization Type")
#         viz_type = st.sidebar.selectbox("Choose Visualization Type", ["Bar Chart", "Line Chart"])
        
#         # Creating a space for charts
#         st.subheader(f"Comparative Visualizations Against '{reference_column}'")
        
#         # Creating a container for charts with multiple columns
#         num_charts = len(numeric_columns) - 1  # Number of charts to display (excluding reference)
#         num_rows = (num_charts + 3) // 4  # Calculate number of rows needed

#         for i in range(num_rows):
#             cols = st.columns(4)  # Create four columns for the charts
#             for j in range(4):
#                 chart_index = i * 4 + j
#                 if chart_index < num_charts:  # Ensure we don't exceed the number of columns
#                     col = cols[j]
#                     with col:
#                         # Get the current column for comparison
#                         col_to_compare = numeric_columns[chart_index + 1]
#                         fig, ax = plt.subplots()
#                         if viz_type == "Bar Chart":
#                             # Bar chart
#                             sns.barplot(data=df, x=reference_column, y=col_to_compare, ax=ax)
#                             ax.set_title(f'Comparison of {col_to_compare} with {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)
#                         elif viz_type == "Line Chart":
#                             # Line chart
#                             sns.lineplot(data=df, x=reference_column, y=col_to_compare, ax=ax)
#                             ax.set_title(f'Trend of {col_to_compare} with respect to {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)
                        
#                         # Display the plot
#                         st.pyplot(fig)

#     else:
#         st.write("No numeric columns found for comparison.")
    
#     # Adding an expander to show/hide raw data
#     with st.expander("Show Raw Data"):
#         st.write("Here is the raw data you uploaded:")
#         st.write(df)

#         # Let users select specific columns to display
#         selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
#         st.write(df[selected_columns])

#     # Data Summary for numeric columns
#     if df.select_dtypes(include='number').shape[1] > 0:
#         st.subheader("Summary Statistics for Numeric Columns")
#         st.write(df.describe())

# else:
#     st.write("Please upload a CSV file to see the dashboard.")


# ## ========================chart color and types ========================================

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Page configuration
# st.set_page_config(layout="wide")  # To make the layout wider for better visualizations

# # Title and Header
# st.title("Dynamic CSV Data Dashboard")
# st.header("Automated Exploratory Data Analysis")

# # Sidebar for uploading CSV
# st.sidebar.header("Upload your CSV file")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# # Function to load data
# @st.cache_data
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

# # Function to determine available chart types based on data
# def get_available_chart_types(numeric_columns, categorical_columns):
#     available_charts = {
#         "Line Chart": True,
#         "Bar Chart": True,
#         "Area Chart": len(numeric_columns) > 1,  # Area chart requires more than 1 numeric column
#         "Scatter Plot": len(numeric_columns) > 1,  # Scatter plot requires at least 2 numeric columns
#         "Bubble Chart": len(numeric_columns) > 1  # Bubble chart requires at least 2 numeric columns
#     }

#     # Disable Area and Stock charts if data is not suitable
#     if 'Year' in df.columns or 'year' in df.columns:
#         if numeric_columns[0] in ['Data_Value', 'Percentage']:
#             available_charts['Area Chart'] = False  # Area charts are often not useful for time series

#     return available_charts

# # If file is uploaded, process the data
# if uploaded_file is not None:
#     df = load_data(uploaded_file)

#     # Detect numeric and categorical columns
#     numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
#     categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

#     # Determine available chart types
#     available_charts = get_available_chart_types(numeric_columns, categorical_columns)

#     # Ensure there is at least one numeric column for reference
#     if len(numeric_columns) > 0:
#         reference_column = numeric_columns[0]  # Use the first numeric column as the reference

#         # Sidebar for selecting visualization type
#         st.sidebar.header("Select Visualization Options")
        
#         # Filter out unavailable chart types
#         viz_type = st.sidebar.selectbox("Choose Visualization Type", 
#                                           [chart for chart, available in available_charts.items() if available])

#         chart_color = st.sidebar.color_picker("Select Chart Color", "#1f77b4")  # Default color

#         # Creating a space for charts
#         st.subheader(f"Comparative Visualizations Against '{reference_column}'")
        
#         # Creating a container for charts with multiple columns
#         num_charts = len(numeric_columns) - 1  # Number of charts to display (excluding reference)
#         num_rows = (num_charts + 3) // 4  # Calculate number of rows needed

#         for i in range(num_rows):
#             cols = st.columns(4)  # Create four columns for the charts
#             for j in range(4):
#                 chart_index = i * 4 + j
#                 if chart_index < num_charts:  # Ensure we don't exceed the number of columns
#                     col = cols[j]
#                     with col:
#                         # Get the current column for comparison
#                         col_to_compare = numeric_columns[chart_index + 1]
#                         fig, ax = plt.subplots()
                        
#                         # Select the appropriate chart type
#                         if viz_type == "Bar Chart":
#                             sns.barplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
#                             ax.set_title(f'Comparison of {col_to_compare} with {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)

#                         elif viz_type == "Line Chart":
#                             sns.lineplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
#                             ax.set_title(f'Trend of {col_to_compare} with respect to {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)

#                         elif viz_type == "Area Chart":
#                             sns.lineplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
#                             ax.fill_between(df[reference_column], df[col_to_compare], color=chart_color, alpha=0.4)
#                             ax.set_title(f'Area Chart of {col_to_compare} with {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)

#                         elif viz_type == "Scatter Plot":
#                             sns.scatterplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
#                             ax.set_title(f'Scatter Plot of {col_to_compare} vs {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)

#                         elif viz_type == "Bubble Chart":
#                             # Assuming we want to use the reference column for x-axis and col_to_compare for y-axis
#                             sns.scatterplot(data=df, x=reference_column, y=col_to_compare, ax=ax, 
#                                             size=df[col_to_compare], sizes=(20, 500), color=chart_color)
#                             ax.set_title(f'Bubble Chart of {col_to_compare} vs {reference_column}')
#                             ax.set_xlabel(reference_column)
#                             ax.set_ylabel(col_to_compare)

#                         # Display the plot
#                         st.pyplot(fig)

#     else:
#         st.write("No numeric columns found for comparison.")
    
#     # Adding an expander to show/hide raw data
#     with st.expander("Show Raw Data Ad Filter As Per Need"):
#         st.write("Here is the raw data you uploaded:")
#         st.write(df)

#         # Let users select specific columns to display
#         selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
#         st.write(df[selected_columns])

#     # Data Summary for numeric columns
#     if df.select_dtypes(include='number').shape[1] > 0:
#         st.subheader("Summary Statistics for Numeric Columns")
#         st.write(df.describe())

# else:
#     st.write("Please upload a CSV file to see the dashboard.")




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(layout="wide")  # To make the layout wider for better visualizations

# Title and Header
st.title("Dynamic CSV Data Dashboard")
st.header("Automated Exploratory Data Analysis")

# Sidebar for Company Logo
st.sidebar.image("images/nap_york.png", width=200)  # Replace with the path to your logo image

# Sidebar for uploading CSV
st.sidebar.header("Upload your CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Function to load data
@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to determine available chart types based on data
def get_available_chart_types(numeric_columns, categorical_columns):
    available_charts = {
        "Line Chart": True,
        "Bar Chart": True,
        "Area Chart": len(numeric_columns) > 1,  # Area chart requires more than 1 numeric column
        "Scatter Plot": len(numeric_columns) > 1,  # Scatter plot requires at least 2 numeric columns
        "Bubble Chart": len(numeric_columns) > 1  # Bubble chart requires at least 2 numeric columns
    }

    # Disable Area and Stock charts if data is not suitable
    if 'Year' in df.columns or 'year' in df.columns:
        if numeric_columns[0] in ['Data_Value', 'Percentage']:
            available_charts['Area Chart'] = False  # Area charts are often not useful for time series

    return available_charts

# If file is uploaded, process the data
if uploaded_file is not None:
    df = load_data(uploaded_file)

    # Detect numeric and categorical columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Determine available chart types
    available_charts = get_available_chart_types(numeric_columns, categorical_columns)

    # Ensure there is at least one numeric column for reference
    if len(numeric_columns) > 0:
        reference_column = numeric_columns[0]  # Use the first numeric column as the reference

        # Sidebar for selecting visualization type
        st.sidebar.header("Select Visualization Options")
        
        # Filter out unavailable chart types
        viz_type = st.sidebar.selectbox("Choose Visualization Type", 
                                          [chart for chart, available in available_charts.items() if available])

        chart_color = st.sidebar.color_picker("Select Chart Color", "#1f77b4")  # Default color

        # Sidebar for selecting columns to display
        selected_columns = st.sidebar.multiselect("Select Columns to Display", df.columns.tolist(), default=df.columns.tolist())

        # Creating a space for charts
        st.subheader(f"Comparative Visualizations Against '{reference_column}'")
        
        # Creating a container for charts with multiple columns
        num_charts = len(numeric_columns) - 1  # Number of charts to display (excluding reference)
        num_rows = (num_charts + 3) // 4  # Calculate number of rows needed

        for i in range(num_rows):
            cols = st.columns(4)  # Create four columns for the charts
            for j in range(4):
                chart_index = i * 4 + j
                if chart_index < num_charts:  # Ensure we don't exceed the number of columns
                    col = cols[j]
                    with col:
                        # Get the current column for comparison
                        col_to_compare = numeric_columns[chart_index + 1]
                        fig, ax = plt.subplots()
                        
                        # Select the appropriate chart type
                        if viz_type == "Bar Chart":
                            sns.barplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
                            ax.set_title(f'Comparison of {col_to_compare} with {reference_column}')
                            ax.set_xlabel(reference_column)
                            ax.set_ylabel(col_to_compare)

                        elif viz_type == "Line Chart":
                            sns.lineplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
                            ax.set_title(f'Trend of {col_to_compare} with respect to {reference_column}')
                            ax.set_xlabel(reference_column)
                            ax.set_ylabel(col_to_compare)

                        elif viz_type == "Area Chart":
                            sns.lineplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
                            ax.fill_between(df[reference_column], df[col_to_compare], color=chart_color, alpha=0.4)
                            ax.set_title(f'Area Chart of {col_to_compare} with {reference_column}')
                            ax.set_xlabel(reference_column)
                            ax.set_ylabel(col_to_compare)

                        elif viz_type == "Scatter Plot":
                            sns.scatterplot(data=df, x=reference_column, y=col_to_compare, ax=ax, color=chart_color)
                            ax.set_title(f'Scatter Plot of {col_to_compare} vs {reference_column}')
                            ax.set_xlabel(reference_column)
                            ax.set_ylabel(col_to_compare)

                        elif viz_type == "Bubble Chart":
                            # Assuming we want to use the reference column for x-axis and col_to_compare for y-axis
                            sns.scatterplot(data=df, x=reference_column, y=col_to_compare, ax=ax, 
                                            size=df[col_to_compare], sizes=(20, 500), color=chart_color)
                            ax.set_title(f'Bubble Chart of {col_to_compare} vs {reference_column}')
                            ax.set_xlabel(reference_column)
                            ax.set_ylabel(col_to_compare)

                        # Display the plot
                        st.pyplot(fig)

        # Adding an expander to show/hide raw data
        with st.expander("Show Raw Data Ad Filter As Per Need"):
            st.write("Here is the raw data you uploaded:")
            st.write(df[selected_columns])  # Display only selected columns

        # Data Summary for numeric columns
        if df.select_dtypes(include='number').shape[1] > 0:
            st.subheader("Summary Statistics for Numeric Columns")
            st.write(df.describe())

else:
    st.write("Please upload a CSV file to see the dashboard.")
