<h2>Overview</h2>
<p>This project is a web-based application for Air Quality Index (AQI) prediction and analysis, built using <strong>Gradio, Streamlit, Pandas, Seaborn, and Matplotlib</strong>. The application allows users to:</p>
<ul>
    <li>Predict AQI values and categories based on Country and City.</li>
    <li>Upload custom CSV datasets for AQI predictions.</li>
    <li>Perform data analysis to visualize pollution levels in different cities.</li>
</ul>

<h2>Features</h2>
<ul>
    <li>AQI Prediction: Predicts AQI based on given Country and City using trained models.</li>
    <li>Data Upload & Processing: Accepts CSV files containing AQI-related data.</li>
    <li>Visualization: Analyzes pollution levels and generates bar charts for insights.</li>
    <li>Dual UI: User-friendly web interface with <strong>Gradio</strong> and <strong>Streamlit</strong> for interactive analysis.</li>
</ul>

<h2>Tech Stack</h2>
<ul>
    <li>Python</li>
    <li>Gradio & Streamlit (for web interface)</li>
    <li>Pandas (for data processing)</li>
    <li>Seaborn & Matplotlib (for visualization)</li>
    <li>Joblib (for loading pre-trained models)</li>
</ul>

<h2>Installation & Usage</h2>

<h3>1. Install Dependencies</h3>
<pre><code>pip install gradio streamlit pandas seaborn matplotlib joblib</code></pre>

<h3>2. Run the Application</h3>
<p>For Gradio interface:</p>
<pre><code>python app.py</code></pre>
<p>For Streamlit interface:</p>
<pre><code>streamlit run webapp.py</code></pre>
<p>The chosen interface will launch in your browser.</p>

<h2>Model Training & Visualization</h2>
<p>The **ml_model.ipynb** file is used to generate the models <code>classifier_pipeline.pkl</code> and <code>regressor_pipeline.pkl</code>, which are utilized in AQI prediction.</p>
<p>Additionally, the **Visualization 1,Visualization 2,Visualization 3,Visualization 4** files contain visualizations of the dataset on which the model is trained, providing insights into air pollution trends.</p>
