Emotion Detection in Text with Artificial Intelligence

This repository contains an artificial intelligence model for detecting emotions in text. The model is developed using TensorFlow and Streamlit for the user interface.

Getting Started

To get started, clone this repository to your local machine:

git clone https://github.com/yourusername/emotion-detection.git

Prerequisites

Before running the application, you need to install the required dependencies. Start by installing the NLTK library for text preprocessing:

pip install nltk

Then, run the following commands to download additional resources for NLTK:

python -m nltk.downloader stopwords

Next, you'll need to install Streamlit and TensorFlow. You can install them using pip:

pip install streamlit tensorflow

Running the Application

After installing the dependencies, navigate to the project directory and run the Streamlit app:

streamlit run app.py

This will start the Streamlit server, and you can access the application in your web browser.

Usage

Once the application is running, you can enter text into the sidebar input field and click the "Submit" button to see the predicted emotion. The model will analyze the text and display its prediction along with the confidence score.

Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
