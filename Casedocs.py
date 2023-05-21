import zipfile
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import string

#Extract the contents of the zip file
zip_path = r"D:\Internship\Project work CDS\AILA_2019_dataset.zip"
extract_folder = r"D:\Internship\Project work CDS\cases_folder"

#Check if the extraction folder exists, create it if necessary
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)

#Extract the zip file to the extraction folder
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

#Preprocess the case documents
case_folder = os.path.join(extract_folder, 'Object_casedocs')
case_files = os.listdir(case_folder)
corpus = []

for case_file in case_files:
    case_file_path = os.path.join(case_folder, case_file)
    with open(case_file_path, 'rb') as file:
        case_text = file.read().decode('utf-8', errors='ignore')
        #Perform preprocessing steps on case_text
        #Extract case title, case number, etc.
        #Store the preprocessed information as needed
        corpus.append(case_text)

#Vectorize the case documents using TF-IDF
vectorizer = TfidfVectorizer()
case_vectors = vectorizer.fit_transform(corpus)

#Process the query
query = 'Your query text'

query_lower = query.lower()  #Convert to lowercase
query_processed = query_lower.translate(str.maketrans('', '', string.punctuation))  #Remove punctuation
#Preprocess the query text similar to the case documents
preprocessed_query = query_processed
query_vector = vectorizer.transform([preprocessed_query])

#Calculate similarity scores using cosine similarity
similarity_scores = cosine_similarity(query_vector, case_vectors)

#Retrieve the most similar/relevant cases
num_results = 5  #Number of top-ranked results to retrieve

top_indices = np.argsort(similarity_scores)[0][-num_results:][::-1]
top_cases = [case_files[i] for i in top_indices]

#Print the top relevant cases
for case in top_cases:
    print(case)
