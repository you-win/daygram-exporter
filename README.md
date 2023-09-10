# Daygram Exporter

An exporter for [Daygram](https://play.google.com/store/apps/details?id=net.saltycrackers.daygram), a minimalist
journaling app for mobile devices.

The app has seemingly been abandoned, so it's now impossible to export to text file or email. Luckily,
Dropbox backups still work. These backups are in the form of a [SQLite](https://www.sqlite.org/index.html)
database and are not immediately viewable.

## Prerequisites

Python 3.6+ (any version of Python3 will probably work)

## Usage

`python daygram_exporter.py SQLITE_DB_FILE [--output FILE_PATH]`

1. Clone this repository (or just copy the python script at `daygram-exporter/daygram_exporter.py` into a file)
2. From a terminal, run `python daygram_exporter.py SQLITE_DB_FILE [--output FILE_PATH]`
    - `SQLITE_DB_FILE` is an absolute or relative file path to the Daygram sqlite db
    - Optionally, `--output FILE_PATH` can be passed to specify the output file
        - By default, a file is created in the current directory named `daygram_exported.txt`

## Example

Running the below command (assuming `daygram.sqlite` is a file in the user's `Downloads` folder):

`python daygram_exporter.py ~/Downloads/daygram.sqlite --output DaygramOutput.txt`

A new file called `DaygramOutput.txt` will be created with contents that look like:

```
---
Date: YYYY-MM-DD
Created: YYYY-MM-DD hh:mm:ss
Updated: YYYY-MM-DD hh:mm:ss
The actual journal entry text.
```

## License

MPL-2.0
