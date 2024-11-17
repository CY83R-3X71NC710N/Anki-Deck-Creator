import requests
import json

def get_all_decks():
    request_payload = {
        "action": "deckNames",
        "version": 6
    }
    response = requests.post('http://localhost:8765', json=request_payload)
    return response.json().get('result', [])

def get_all_note_ids(deck_name):
    request_payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f"deck:{deck_name}"
        }
    }
    response = requests.post('http://localhost:8765', json=request_payload)
    return response.json().get('result', [])

def get_note_info(note_ids):
    request_payload = {
        "action": "notesInfo",
        "version": 6,
        "params": {
            "notes": note_ids
        }
    }
    response = requests.post('http://localhost:8765', json=request_payload)
    return response.json().get('result', [])

def main():
    decks = get_all_decks()
    all_notes = []

    for deck in decks:
        note_ids = get_all_note_ids(deck)
        if note_ids:
            notes = get_note_info(note_ids)
            all_notes.extend(notes)

    for note in all_notes:
        print(json.dumps(note, indent=2))

if __name__ == "__main__":
    main()
