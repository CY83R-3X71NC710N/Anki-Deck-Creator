import genanki
import random
import string

# Function to generate a random string
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Read flashcards from a text file
def read_flashcards(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]  # Remove empty lines and strip whitespace

    flashcards = []
    i = 0
    while i < len(lines):
        if i + 2 < len(lines):
            question = lines[i]
            answer = lines[i+1]
            # Skip the next line as it is a category
            i += 3  # Move to the next set of flashcards
            flashcards.append((question, answer))
        else:
            print(f"Warning: Incomplete flashcard entry starting at line {i+1}")
            break
    return flashcards

# Use the existing Basic model ID
BASIC_MODEL_ID = 1091735104

# Generate random deck name and file name
deck_name = random_string()
file_name = f'{random_string()}.apkg'

# Create a new deck with a random name
deck = genanki.Deck(
  random.randint(1 << 30, 1 << 31),
  deck_name)

# Read flashcards from the text file
flashcards = read_flashcards('flashcards.txt')

# Add flashcards to the deck
for question, answer in flashcards:
  note = genanki.Note(
    model=genanki.Model(BASIC_MODEL_ID, 'Basic'),
    fields=[question, answer])
  deck.add_note(note)

# Create a package and write to a file with a random name
package = genanki.Package(deck)
package.write_to_file(file_name)

print(f'Deck "{deck_name}" has been created and saved as "{file_name}".')
