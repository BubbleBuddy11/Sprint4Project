# Sprint4Project
SDT Sprint Project

# Vehicle Sales Dashboard

This is a web application built using Streamlit to visualize data from a car advertisement dataset.

## Project Description

This project aims to provide additional practice with common software engineering tasks, including creating a virtual environment, developing a web application, and deploying it to a cloud service accessible to the public.

### Dataset

The application uses a dataset of car sales advertisements (`vehicles_us.csv`). The dataset contains information such as price, manufacturer, model, year, odometer, paint color, and whether the vehicle is four wheel drive, among other attributes.

### Features

- **Data Cleaning:** Missing values in the dataset have been handled as part of the preprocessing.
- **Visualizations:**
  - **Data Viewer:** An interactive chart displaying all of the data from this dataset, able to be sorted by each column.
  - **Miles on Vehicle vs. Price by Manufacturer:** A scatter plot depicting the relationship between the odometer readings and vehical prices, sorted by manufacturer using colors.
  - **Distribution of Price:** A histogram showing the distribution of vehicle prices.
  - **Price vs. Days Listed by Manufacturer:** A scatter plot visualizing the relationship between vehicle prices and the number of days a vehicle has been listed, sorted by manufacturer using colors.
  - **Compare Price Distribution Between Vehicle Condition:** A histogram that compares any two vehicle conditions (selected by the user) and compares the prices between the two. There is a checkbox option that when checked, normalizes the histogram.

### Technologies Used

- **Python**: Core programming language used for data manipulation and visualization.
- **Streamlit**: Framework used to build and deploy the interactive web application.
- **Pandas**: Library used for data manipulation and analysis.
- **Plotly Express**: Library used for creating interactive plots.

## Instructions

### Requirements

- Ensure you have Python installed on your local machine.
- Install the required packages listed in `requirements.txt` (pandas, streamlit, plotly.express, etc.).

### Setup

1. **Clone the repository:**
    
bash
    git clone <repository_link>
    cd <repository_directory>
    
2. **Create a virtual environment and activate it:**
    
bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    
3. **Install the required packages:**
    
bash
    pip install -r requirements.txt
    

4. **Run the application:**
    
bash
    streamlit run app.py
    
5. **Access the application:**
    - Open your web browser and go to `http://localhost:8501`.

## Deployment

The application is deployed on Render and is accessible via the following URL: [https://sprint4project-f4d5.onrender.com](https://sprint4project-f4d5.onrender.com)