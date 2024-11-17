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
        lines = [line.strip() for line if line.strip()]  # Remove empty lines and strip whitespace

    flashcards = []
    i = 0
    while i < len(lines):
        categories = []
        # Collect categories
        while i < len(lines) and not lines[i].endswith('?'):
            categories.append(lines[i])
            i += 1
        # Ensure there are enough lines for a question and answer
        if i < len(lines) and lines[i].endswith('?'):
            question = lines[i]
            i += 1
            if i < len(lines):
                answer = lines[i]
                flashcards.append((question, answer, categories))
                i += 1
            else:
                print(f"Warning: Missing answer for question starting at line {i+1}")
        else:
            print(f"Warning: Incomplete flashcard entry starting at line {i+1}")
            break
    return flashcards

# Define the model for the flashcards
model = genanki.Model(
  1607392319,
  'AnkiGen',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Categories'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}<br><br><i>{{Categories}}</i>',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

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
for question, answer, categories in flashcards:
  note = genanki.Note(
    model=model,
    fields=[question, answer, ', '.join(categories)])
  deck.add_note(note)

# Create a package and write to a file with a random name
package = genanki.Package(deck)
package.write_to_file(file_name)

print(f'Deck "{deck_name}" has been created and saved as "{file_name}".')
