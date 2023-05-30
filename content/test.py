import os

folder_path = "posts"  # Replace with the actual folder path

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)

        # Read the contents of the file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Check if the "ShowCodeCopyButtons: true" line already exists in the file
        if "ShowCodeCopyButtons: true\n" in lines:
            print(f"Skipping {filename} as it already contains the 'ShowCodeCopyButtons: true' line.")
            continue

        # Find the index of the last "---" line
        last_separator_index = -1
        for i, line in enumerate(lines):
            if line.strip() == "---":
                last_separator_index = i

        # Insert the "ShowCodeCopyButtons: true" line before the last "---" line
        if last_separator_index != -1:
            lines.insert(last_separator_index, "ShowCodeCopyButtons: true\n")

            # Write the modified contents back to the file
            with open(file_path, "w") as file:
                file.writelines(lines)

            print(f"Updated {filename} successfully.")
        else:
            print(f"No '---' separator found in {filename}. Skipping the file.")
