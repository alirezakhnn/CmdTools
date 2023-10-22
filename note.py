# notes.py

# Function to display a list of notes


def display_notes(notes):
    print("=== Notes ===")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}")
    print()

# Function to add a new note
def add_note(notes, new_note):
    notes.append(new_note)
    print("Note added successfully!\n")

# Function to edit a note
def edit_note(notes, index, new_note):
    if index >= 0 and index < len(notes):
        notes[index] = new_note
        print("Note edited successfully!\n")
    else:
        print("Invalid note index.\n")

# Function to delete a note
def delete_note(notes, index):
    if index >= 0 and index < len(notes):
        del notes[index]
        print("Note deleted successfully!\n")
    else:
        print("Invalid note index.\n")

# Function to save notes to a text file
def save_notes_to_file(notes, filename):
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")
    print(f"Notes saved to {filename}.\n")

# Function to load notes from a text file
def load_notes_from_file(filename):
    notes = []
    try:
        with open(filename, "r") as file:
            for line in file:
                note = line.strip()
                if note:
                    notes.append(note)
        print(f"Notes loaded from {filename}.\n")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty notes.\n")
    return notes

# Main program loop
def main():
    filename = "notes.txt"
    notes = load_notes_from_file(filename)

    while True:
        display_notes(notes)
        print("Menu:")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. Save Notes")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_note = input("Enter the new note: ")
            add_note(notes, new_note)
        elif choice == "2":
            index = int(input("Enter the note index to edit: ")) - 1
            new_note = input("Enter the new note: ")
            edit_note(notes, index, new_note)
        elif choice == "3":
            index = int(input("Enter the note index to delete: ")) - 1
            delete_note(notes, index)
        elif choice == "4":
            save_notes_to_file(notes, filename)
        elif choice == "5":
            print("Exiting program...")
            save_notes_to_file(notes, filename)  # Save notes before exiting
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the main program
if __name__ == "__main__":
    main()
