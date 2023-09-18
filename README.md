# Job-Recommendation-System
Job Recommendation System

This is a simple job recommendation system that suggests job titles based on a given job title using text similarity. The system uses a dataset of job descriptions and applies text preprocessing techniques to recommend similar job titles.

## Dataset

The system uses a dataset from a CSV file called "Combined_Jobs_Final.csv". This dataset contains various attributes related to job postings, including job titles, job descriptions, company names, and more.

### Dataset Preprocessing

1. **Data Cleaning**: The dataset is cleaned to remove any special characters and non-alphanumeric characters from the job descriptions and other text fields.

2. **Text Processing**:
   - **Tokenization**: The job descriptions are tokenized into words.
   - **Lowercasing**: All text is converted to lowercase to ensure consistency.
   - **Stopword Removal**: Common stopwords are removed from the text data.
   - **Stemming**: The words are stemmed to reduce them to their root form.

3. **Feature Creation**: A new feature called `clean_text` is created by combining the cleaned job description, title, and position fields.

## Text Vectorization

The text data in the `clean_text` column is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. This step converts the text data into numerical format, making it suitable for similarity calculation.

## Similarity Calculation

Cosine similarity is used to calculate the similarity between the job descriptions. Cosine similarity measures the cosine of the angle between two non-zero vectors, which is a common method for text similarity calculation.

## Recommendation System

The recommendation system works as follows:

1. The user selects a job title as input.
2. The system finds the index of the selected job title in the dataset.
3. Cosine similarities between the selected job and all other jobs in the dataset are calculated.
4. The most similar job titles are recommended based on their cosine similarity scores.

## Usage

To use the job recommendation system, you can interact with it through a web application created using Streamlit. The application allows you to select a job title, and it will display a list of recommended job titles based on the selected one.
![image](https://github.com/LikhithaAralimara/Job-Recommendation-System/assets/128489410/0353edca-e02d-4a2f-be88-017249f1cdec)

![image](https://github.com/LikhithaAralimara/Job-Recommendation-System/assets/128489410/9fe3a857-82a6-4697-a02f-bb8f72a6d709)


### Running the Application

1. Make sure you have Streamlit and the required libraries installed.
2. Run the `app.py` script.
3. The web application will open, allowing you to search for job recommendations.

## Files Included

- `app.py`: The Streamlit web application for interacting with the recommendation system.
- `df.pkl`: A serialized version of the processed DataFrame containing job data.
- `similarity.pkl`: A serialized version of the calculated cosine similarity matrix.
- `Combined_Jobs_Final.csv`: The original dataset used for job recommendations.

## Dataset

The system uses a dataset from ["Combined_Jobs_Final.csv"](https://www.kaggle.com/datasets/kandij/job-recommendation-datasets?select=Combined_Jobs_Final.csv). This dataset contains various attributes related to job postings, including job titles, job descriptions, company names, and more.


## Dependencies

- Python 3.x
- pandas
- numpy
- nltk
- scikit-learn
- Streamlit



