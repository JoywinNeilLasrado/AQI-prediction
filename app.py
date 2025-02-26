import gradio as gr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load the saved models
regressor_pipeline = joblib.load("regressor_pipeline.pkl")
classifier_pipeline = joblib.load("classifier_pipeline.pkl")

# Function to predict AQI using only Country and City
def predict_aqi_with_defaults(country, city, dataset):
    matched_data = dataset[(dataset['Country'] == country) & (dataset['City'] == city)]
    if matched_data.empty:
        return "No matching data found for the specified Country and City."
    
    row = matched_data.iloc[0]
    
    input_data = pd.DataFrame({
        'Country': [country],
        'City': [city],
        'CO AQI Value': [row.get('CO AQI Value', dataset['CO AQI Value'].mean())],
        'Ozone AQI Value': [row.get('Ozone AQI Value', dataset['Ozone AQI Value'].mean())],
        'NO2 AQI Value': [row.get('NO2 AQI Value', dataset['NO2 AQI Value'].mean())],
        'PM2.5 AQI Value': [row.get('PM2.5 AQI Value', dataset['PM2.5 AQI Value'].mean())],
        'lat': [row.get('lat', dataset['lat'].mean())],
        'lng': [row.get('lng', dataset['lng'].mean())]
    })
    
    aqi_value = regressor_pipeline.predict(input_data)[0]
    aqi_category = classifier_pipeline.predict(input_data)[0]
    return f"Predicted AQI Value: {aqi_value:.2f}\nPredicted AQI Category: {aqi_category}"

# Function for Upload and Prediction
def upload_and_predict(file_path, country, city):
    dataset = pd.read_csv(file_path)
    required_columns = ['Country', 'City', 'CO AQI Value', 'Ozone AQI Value', 
                        'NO2 AQI Value', 'PM2.5 AQI Value', 'lat', 'lng']
    
    if not all(col in dataset.columns for col in required_columns):
        return f"Dataset is missing required columns: {', '.join(required_columns)}"
    
    return predict_aqi_with_defaults(country, city, dataset)

# Function to perform analysis
def analyze_data(file_path):
    dataset = pd.read_csv(file_path)
    
    # Example analysis: Most Polluted Cities by AQI
    top_cities_data = dataset.groupby('City')['AQI Value'].mean().sort_values(ascending=False).head(10).reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=top_cities_data, x='City', y='AQI Value', ci=None, ax=ax)
    ax.set_title('Top 10 Polluted Cities by AQI Value')
    ax.set_xlabel('City')
    ax.set_ylabel('Average AQI Value')
    ax.tick_params(axis='x', rotation=45)
    
    # Save the figure and return as output
    plt.close(fig)  # To prevent duplicate plotting
    return fig

# Define Gradio interface
def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## AQI Prediction and Analysis")
        
        with gr.Tab("Home"):
            file_input = gr.File(label="Upload Dataset (CSV)", type="filepath")
            country_input = gr.Textbox(label="Enter Country")
            city_input = gr.Textbox(label="Enter City")
            prediction_output = gr.Textbox(label="Prediction Output", interactive=False)
            
            file_input.change(upload_and_predict, inputs=[file_input, country_input, city_input], outputs=prediction_output)
        
        with gr.Tab("Analysis"):
            file_input_analysis = gr.File(label="Upload Dataset (CSV) for Analysis", type="filepath")
            analysis_output = gr.Plot(label="Pollution Analysis")
            
            file_input_analysis.change(analyze_data, inputs=file_input_analysis, outputs=analysis_output)
    
    return demo

# Launch the app
if __name__ == "__main__":
    demo = create_interface()
    demo.launch()
