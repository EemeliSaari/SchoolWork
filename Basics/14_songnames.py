# Purpose: learn how to use os library

import os


def fix_filenames(directory_input):

    for file in os.listdir(directory_input):

        file_type = file.split(".")
        if file_type[1] == "mp3":
            parts = file_type[0].split("-")
            try:
                int(parts[0])

                if len(parts) > 2:
                    new_text = parts[2] + "-" + parts[1] + ".mp3"
                    os.renames(os.path.join(directory_input,file),
                               os.path.join(directory_input,new_text))

            except ValueError:
                pass
