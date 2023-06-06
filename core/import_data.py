import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from product.models import GenreTable

def import_data():
    file_path = 'file1.csv'  # Update with the path to your CSV file

    with open("file1.csv", 'r') as file:
        csv_reader = csv.reader(file)
        # next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            id, genre_name = row
            
            # Print the record in the terminal
            print(f"id: {id}")
            print(f"genre_name: {genre_name}")

            print()  # Empty line for readability
            
            # Get or create the GenreTable instance based on the provided id
            genre, created = GenreTable.objects.get_or_create(
                id=int(id),
                defaults={'genre_name': genre_name}
            )
            if not created:
                # If the instance already exists, update the genre_name field
                genre.genre_name = genre_name
                genre.save()

if __name__ == '__main__':
    import_data()