"""
Backup Utility
• Objective: Use file operations, modules, sets, and error handling to build a smart
backup tool.
• Task: Copy files to a backup folder while skipping duplicates and logging operations.
"""
import os
import shutil

copied_files = set()


def backup_file(file_name):

    try:

        backup_folder = "backup"

        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)

        if file_name in copied_files:

            with open("backup.log", "a") as log:

                log.write(f"Skipped Duplicate: {file_name}\n")

            print("Duplicate skipped")

            return

        shutil.copy(file_name, backup_folder)

        copied_files.add(file_name)

        with open("backup.log", "a") as log:

            log.write(f"Copied: {file_name}\n")

        print("Backup completed")

    except FileNotFoundError:

        print("File not found")
