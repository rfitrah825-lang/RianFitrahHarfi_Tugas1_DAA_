
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "google_books_dataset.csv"

# Load the latest version
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "mihikaajayjadhav/books-dataset-15k-books-across-100-categories",
    file_path,
)

print("First 5 records:", df.head())
